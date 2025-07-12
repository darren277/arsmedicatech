import ReactDOM from 'react-dom';
import App from './App';
import './index.css';
// import * as serviceWorker from './serviceWorker';

import * as Sentry from '@sentry/react';

import { SENTRY_DSN } from './env_vars';

Sentry.init({
  dsn: SENTRY_DSN,
  // Setting this option to true will send default PII data to Sentry.
  // For example, automatic IP address collection on events
  sendDefaultPii: true,
});

ReactDOM.render(<App />, document.getElementById('root'));
// ReactDOM.render(<h3>Test</h3>, document.getElementById('root'));

// serviceWorker.unregister();
