import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createHash, randomBytes } from 'node:crypto';
import Fastify from 'fastify';
import { buildApp } from './app.mjs';

async function fixture(t) {
  const provider = Fastify();
  const codes = new Map();
  let exchanges = 0;
  provider.addContentTypeParser('application/x-www-form-urlencoded', { parseAs: 'string' }, (_, body, done) => done(null, Object.fromEntries(new URLSearchParams(body))));
  provider.post('/token', async (request, reply) => {
    exchanges++;
    const expected = codes.get(request.body.code);
    codes.delete(request.body.code);
    if (!expected || !request.body.code_verifier || createHash('sha256').update(request.body.code_verifier).digest('base64url') !== expected) {
      return reply.code(400).send({ error: 'invalid_grant' });
    }
    return { access_token: 'fixture-access-token', token_type: 'Bearer', expires_in: 300 };
  });
  provider.get('/resource', (request, reply) => request.headers.authorization === 'Bearer fixture-access-token'
    ? { value: 'private fixture data', internal: 'must not be forwarded' }
    : reply.code(401).send({ error: 'invalid_token' }));
  await provider.listen({ host: '127.0.0.1', port: 0 });
  t.after(() => provider.close());
  const app = await buildApp({ providerUrl: provider.listeningOrigin, callbackUri: 'http://127.0.0.1:3000/callback', clientId: 'fixture-client', clientSecret: 'fixture-client-secret', sessionSecret: randomBytes(32).toString('hex'), localDevelopment: true });
  t.after(() => app.close());
  const cookies = {};
  const inject = async (url, options = {}) => {
    const response = await app.inject({ url, cookies, ...options });
    for (const item of response.cookies) {
      if (item.maxAge === 0 || item.value === '') delete cookies[item.name];
      else cookies[item.name] = item.value;
    }
    return response;
  };
  async function start() {
    const response = await inject('/connect');
    assert.equal(response.statusCode, 302);
    const authorization = new URL(response.headers.location);
    assert.equal(authorization.searchParams.get('code_challenge_method'), 'S256');
    assert.equal(authorization.searchParams.get('redirect_uri'), 'http://127.0.0.1:3000/callback');
    const code = randomBytes(12).toString('hex');
    codes.set(code, authorization.searchParams.get('code_challenge'));
    return { code, state: authorization.searchParams.get('state') };
  }
  return { app, cookies, inject, start, exchanges: () => exchanges };
}
test('PKCE exchange establishes a server session, protects resources and disconnects', async t => {
  const f = await fixture(t);
  assert.equal((await f.inject('/resource')).statusCode, 401);
  const { code, state } = await f.start();
  const oldSession = f.cookies['example-session'];
  const callback = await f.inject(`/callback?code=${code}&state=${state}`);
  assert.equal(callback.statusCode, 302, callback.body);
  assert.notEqual(f.cookies['example-session'], oldSession);
  assert.equal(f.cookies['example-verifier'], undefined);
  assert.equal(callback.body.includes('fixture-access-token'), false);
  assert.deepEqual((await f.inject('/resource')).json(), { value: 'private fixture data' });
  assert.equal((await f.inject('/disconnect', { method: 'POST' })).statusCode, 403);
  assert.equal((await f.inject('/disconnect', { method: 'POST', headers: { origin: 'http://127.0.0.1:3000' } })).statusCode, 204);
  assert.equal((await f.inject('/resource')).statusCode, 401);
});
test('rejects a callback from a different session before exchanging its code', async t => {
  const f = await fixture(t);
  const { code, state } = await f.start();
  const response = await f.app.inject(`/callback?code=${code}&state=${state}`);
  assert.equal(response.statusCode, 400);
  assert.equal(f.exchanges(), 0);
});
test('rejects incorrect state and consumes it', async t => {
  const f = await fixture(t);
  const { code, state } = await f.start();
  assert.equal((await f.inject(`/callback?code=${code}&state=wrong`)).statusCode, 400);
  assert.equal((await f.inject(`/callback?code=${code}&state=${state}`)).statusCode, 400);
  assert.equal(f.exchanges(), 0);
});
test('rejects a missing PKCE verifier and does not establish a session', async t => {
  const f = await fixture(t);
  const { code, state } = await f.start();
  delete f.cookies['example-verifier'];
  assert.equal((await f.inject(`/callback?code=${code}&state=${state}`)).statusCode, 400);
  assert.equal((await f.inject('/connection')).json().connected, false);
});
test('callback cannot be replayed after successful exchange', async t => {
  const f = await fixture(t);
  const { code, state } = await f.start();
  const url = `/callback?code=${code}&state=${state}`;
  assert.equal((await f.inject(url)).statusCode, 302);
  assert.equal((await f.inject(url)).statusCode, 400);
  assert.equal(f.exchanges(), 1);
});
test('rejects unsafe remote HTTP configuration', async () => {
  await assert.rejects(buildApp({ providerUrl: 'http://provider.example', callbackUri: 'http://127.0.0.1:3000/callback', clientId: 'x', clientSecret: 'y', sessionSecret: 'x'.repeat(32), localDevelopment: true }), /HTTPS/);
});
