import { buildApp } from './app.mjs';
// Loopback demonstration only. Integrate a persistent store via buildApp for production.
const app = await buildApp({
  providerUrl: process.env.PROVIDER_URL,
  callbackUri: process.env.CALLBACK_URI ?? 'http://127.0.0.1:3000/callback',
  clientId: process.env.CLIENT_ID,
  clientSecret: process.env.CLIENT_SECRET,
  sessionSecret: process.env.SESSION_SECRET,
  localDevelopment: true,
});
await app.listen({ host: '127.0.0.1', port: 3000 });
for (const signal of ['SIGINT', 'SIGTERM']) process.once(signal, () => { void app.close(); });
