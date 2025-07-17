//const API_URL = 'https://demo.arsmedicatech.com';
const API_URL = process.env.API_URL || 'http://127.0.0.1:3123';

const SENTRY_DSN =
  'https://aec01cd03a9a408398ec656d4e7f5ddb@o4509655831412736.ingest.us.sentry.io/4509655843799040';

const LIVE_KIT_TOKEN_URL = 'http://localhost:5001';
const LIVE_KIT_SERVER_URL = 'http://localhost:7880';

export { API_URL, LIVE_KIT_SERVER_URL, LIVE_KIT_TOKEN_URL, SENTRY_DSN };

