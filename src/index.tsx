import ReactDOM from 'react-dom';
import App from './App';
import './index.css';
// import * as serviceWorker from './serviceWorker';

import * as Sentry from '@sentry/react';

import { SENTRY_DSN } from './env_vars';

if (!SENTRY_DSN) {
  throw new Error('SENTRY_DSN environment variable is not set');
}

Sentry.init({
  dsn: SENTRY_DSN,
  // Setting this option to true will send default PII data to Sentry.
  // For example, automatic IP address collection on events
  sendDefaultPii: true,
});

// This is for plugins to register
import React from 'react';
window.React = React;

ReactDOM.render(<App />, document.getElementById('root'));
// ReactDOM.render(<h3>Test</h3>, document.getElementById('root'));

// serviceWorker.unregister();
