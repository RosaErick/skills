import Fastify from 'fastify';
import cookie from '@fastify/cookie';
import session from '@fastify/session';
import oauth2 from '@fastify/oauth2';
import { randomBytes, timingSafeEqual } from 'node:crypto';

export async function buildApp({ providerUrl, callbackUri, clientId, clientSecret,
  sessionSecret, sessionStore, localDevelopment = false }) {
  for (const [name, value] of Object.entries({ providerUrl, callbackUri, clientId, clientSecret, sessionSecret })) {
    if (!value) throw new Error(`Missing ${name}`);
  }
  if (sessionSecret.length < 32) throw new Error('sessionSecret must have at least 32 characters');
  for (const value of [providerUrl, callbackUri]) {
    const url = new URL(value);
    const local = ['localhost', '127.0.0.1', '[::1]'].includes(url.hostname);
    if (url.protocol !== 'https:' && !(localDevelopment && local && url.protocol === 'http:')) {
      throw new Error('HTTPS is required except for explicit loopback development');
    }
  }
  if (!localDevelopment && !sessionStore) throw new Error('A production session store is required');
  const secure = new URL(callbackUri).protocol === 'https:';
  const app = Fastify({ logger: false });
  await app.register(cookie);
  await app.register(session, {
    secret: sessionSecret,
    cookieName: secure ? '__Host-example-session' : 'example-session',
    cookie: { secure, httpOnly: true, sameSite: 'lax', path: '/', maxAge: 30 * 60 * 1000 },
    saveUninitialized: false,
    ...(sessionStore ? { store: sessionStore } : {}),
  });
  await app.register(oauth2, {
    name: 'provider',
    scope: ['read'],
    credentials: {
      client: { id: clientId, secret: clientSecret },
      auth: { authorizeHost: providerUrl, authorizePath: '/authorize', tokenHost: providerUrl, tokenPath: '/token' },
    },
    startRedirectPath: '/connect',
    callbackUri,
    pkce: 'S256',
    cookie: { secure, httpOnly: true, sameSite: 'lax', path: '/' },
    redirectStateCookieName: secure ? '__Host-example-state' : 'example-state',
    verifierCookieName: secure ? '__Host-example-verifier' : 'example-verifier',
    generateStateFunction(request) {
      const state = randomBytes(32).toString('hex');
      request.session.oauthState = state;
      return state;
    },
    checkStateFunction(request, callback) {
      const expected = request.session.oauthState;
      const supplied = request.query.state;
      delete request.session.oauthState; // consume even when the callback fails
      const valid = typeof expected === 'string' && typeof supplied === 'string'
        && Buffer.byteLength(expected) === Buffer.byteLength(supplied)
        && timingSafeEqual(Buffer.from(expected), Buffer.from(supplied));
      callback(valid ? undefined : new Error('Invalid OAuth state'));
    },
  });
  app.get('/callback', async (request, reply) => {
    reply.header('Cache-Control', 'no-store');
    try {
      const { token } = await app.provider.getAccessTokenFromAuthorizationCodeFlow(request, reply);
      if (typeof token.access_token !== 'string' || !token.access_token) throw new Error('Missing access token');
      await request.session.regenerate();
      request.session.accessToken = token.access_token;
      return reply.redirect('/connection');
    } catch {
      return reply.code(400).send({ error: 'oauth_connection_failed' });
    }
  });
  app.get('/connection', async (request, reply) => {
    reply.header('Cache-Control', 'no-store');
    return { connected: Boolean(request.session.accessToken) };
  });
  app.get('/resource', async (request, reply) => {
    reply.header('Cache-Control', 'no-store');
    if (!request.session.accessToken) return reply.code(401).send({ error: 'connection_required' });
    try {
      const response = await fetch(new URL('/resource', providerUrl), {
        headers: { Authorization: `Bearer ${request.session.accessToken}` },
        signal: AbortSignal.timeout(5000),
        redirect: 'error',
      });
      if (response.status === 401) {
        delete request.session.accessToken;
        return reply.code(401).send({ error: 'reconnect_required' });
      }
      if (!response.ok) throw new Error('Upstream failed');
      const data = await response.json();
      return { value: data.value }; // explicitly selected application response
    } catch {
      return reply.code(502).send({ error: 'provider_unavailable' });
    }
  });
  app.post('/disconnect', async (request, reply) => {
    // A same-origin request is required for this state-changing browser endpoint.
    if (request.headers.origin !== new URL(callbackUri).origin) {
      return reply.code(403).send({ error: 'invalid_origin' });
    }
    await request.session.destroy();
    reply.clearCookie(secure ? '__Host-example-session' : 'example-session', { path: '/', secure, httpOnly: true, sameSite: 'lax' });
    return reply.header('Cache-Control', 'no-store').code(204).send();
  });
  await app.ready();
  return app;
}
