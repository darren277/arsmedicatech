import { useEffect, useState } from 'react';
import Joyride from 'react-joyride';
import { Outlet } from 'react-router-dom';
import './App.css';
import ErrorModal, { createErrorModalState } from './components/ErrorModal';
import PatientForm from './components/PatientForm';
import { tourSteps } from './onboarding/tourSteps';
import Dashboard from './pages/Dashboard';
import { EncounterDetail } from './pages/EncounterDetail';
import { EncounterFormPage } from './pages/EncounterForm';
import LabResults from './pages/LabResults';
import OptimalTableDemo from './pages/OptimalTableDemo';
import { PatientDetail } from './pages/PatientDetail';
import { Patients } from './pages/Patients';
import UserNotesPage from './pages/UserNotesPage';

import {
  HealthMetricTracker,
  HealthMetricVisualization,
} from './components/HealthMetricTracker';

import Sidebar from './components/Sidebar';
import Topbar from './components/Topbar';

import Messages from './pages/Messages';
import Schedule from './pages/Schedule';

import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import {
  NotificationProvider,
  useNotificationContext,
} from './components/NotificationContext';
import PatientIntakeForm from './components/PatientIntakeForm';
import Settings from './components/Settings';
import { UserProvider } from './components/UserContext';

import VideoRoom from './components/VideoRoom';
import { API_URL } from './env_vars';
import { usePluginRoutes } from './hooks/usePluginRoutes';
import Administration from './pages/Administration';
import FileUpload from './pages/FileUpload';
import Organization from './pages/Organization';
import RoleDescriptions from './pages/RoleDescriptions';
import UploadDetails from './pages/UploadDetails';
import { pluginAPI } from './services/api';
import logger from './services/logging';
import { PluginRoute } from './types';

function useLoadPlugins() {
  useEffect(() => {
    pluginAPI.getAll().then(plugins => {
      plugins.forEach((plugin: any) => {
        if (plugin.main_js) {
          const script = document.createElement('script');
          script.src = API_URL + `/plugin/${plugin.name}`;
          script.async = true;
          console.log('Loading plugin:', script);
          document.body.appendChild(script);
        }
      });
    });
  }, []);
}

const isTestMode = true;

function Home() {
  logger.debug('Home component rendered');

  // TODO: Make this more programmatically flexible...
  // [AMT-035] User Onboarding Flows
  // This should load when the user first logs in and then update the state to not run again
  // And during e2e testing, it should always be disabled.
  //const isTestMode = process.env.NODE_ENV === 'test' || process.env.DISABLE_TOUR === 'true';
  const [runTour, setRunTour] = useState(!isTestMode);
  const [errorModal, setErrorModal] = useState<{
    isOpen: boolean;
    error: string;
    description: string;
    suggested_action?: string;
  }>({
    isOpen: false,
    error: 'Something went wrong',
    description:
      'An unknown error has occurred. Please return to the home screen. The error has been logged and is being investigated.',
  });

  // Get notification context
  const {
    unreadCount,
    getRecentNotifications,
    markAsRead,
    markAllAsRead,
    clearNotification,
    clearAllNotifications,
  } = useNotificationContext();

  // Handle OAuth callback errors
  useEffect(() => {
    const handleAuthCallback = async () => {
      const urlParams = new URLSearchParams(window.location.search);
      const error = urlParams.get('error');
      const errorDescription = urlParams.get('error_description');
      const suggestedAction = urlParams.get('suggested_action');

      if (error) {
        logger.warn('Auth callback error detected:', {
          error,
          errorDescription,
          suggestedAction,
        });

        // Handle specific Cognito errors
        if (
          error === 'invalid_request' &&
          errorDescription?.includes('email')
        ) {
          setErrorModal(
            createErrorModalState(
              'Email Already Exists',
              'This email address is already registered. Please try signing in instead.',
              'login'
            )
          );
        } else if (error === 'access_denied') {
          setErrorModal(
            createErrorModalState(
              'Access Denied',
              errorDescription || 'Access was denied. Please try again.',
              'home'
            )
          );
        } else if (
          error === 'server_error' ||
          error === 'temporarily_unavailable'
        ) {
          setErrorModal(
            createErrorModalState(
              'Service Unavailable',
              errorDescription ||
                'Authentication service is temporarily unavailable. Please try again later.',
              'home'
            )
          );
        } else {
          setErrorModal(
            createErrorModalState(
              'Authentication Error',
              errorDescription || error,
              suggestedAction || 'home'
            )
          );
        }

        // Clean up the URL
        const newUrl = window.location.pathname;
        window.history.replaceState({}, document.title, newUrl);
      }
    };

    handleAuthCallback();
  }, []);

  const handleCloseErrorModal = () => {
    setErrorModal(prev => ({ ...prev, isOpen: false }));
  };

  return (
    <div className="App app-container">
      <ErrorModal
        isOpen={errorModal.isOpen}
        error={errorModal.error}
        description={errorModal.description}
        suggested_action={errorModal.suggested_action}
        onClose={handleCloseErrorModal}
      />

      <Sidebar />
      <div className="main-container">
        <Topbar
          unreadCount={unreadCount}
          recentNotifications={getRecentNotifications(5)}
          onMarkAsRead={markAsRead}
          onMarkAllAsRead={markAllAsRead}
          onClearNotification={clearNotification}
          onClearAll={clearAllNotifications}
        />

        <div className="main-content">
          <main>
            {/* This is where the nested routes will render */}
            <Outlet />
          </main>
          <Joyride
            steps={tourSteps}
            continuous={true} // let the user move from step to step seamlessly
            scrollToFirstStep={true}
            showProgress={true} // display step count
            showSkipButton={true} // allow skipping
            run={runTour} // start or stop the tour
            callback={data => {
              const { status } = data;
              if (status === 'finished' || status === 'skipped') {
                setRunTour(false);
              }
            }}
            styles={{
              options: { zIndex: 10000 },
            }}
          />
        </div>
      </div>
    </div>
  );
}

function About() {
  return (
    <div>
      <h1>About</h1>
      <p>This is the about page.</p>
    </div>
  );
}

function Contact() {
  return (
    <div>
      <h1>Contact</h1>
      <p>This is the contact page.</p>
    </div>
  );
}

function ErrorPage() {
  return (
    <div>
      <h1>404</h1>
      <p>Page not found.</p>
    </div>
  );
}

const baseRoutes: PluginRoute[] = [
  { index: true, element: <Dashboard /> },
  { path: 'about', element: <About /> },
  { path: 'contact', element: <Contact /> },
  { path: 'patients', element: <Patients /> },
  { path: 'patients/new', element: <PatientForm /> },
  { path: 'patients/:patientId', element: <PatientDetail /> },
  { path: 'patients/:patientId/edit', element: <PatientForm /> },
  {
    path: 'patients/:patientId/encounters/new',
    element: <EncounterFormPage />,
  },
  { path: 'encounters/:encounterId', element: <EncounterDetail /> },
  { path: 'encounters/:encounterId/edit', element: <EncounterFormPage /> },
  { path: 'intake/:patientId', element: <PatientIntakeForm /> },
  { path: 'schedule', element: <Schedule /> },
  { path: 'messages', element: <Messages /> },
  { path: 'settings', element: <Settings /> },
  { path: 'lab-results', element: <LabResults /> },

  { path: 'health-metrics', element: <HealthMetricTracker /> },
  {
    path: 'health-metrics-visualization',
    element: <HealthMetricVisualization />,
  },

  { path: 'optimal-table-demo', element: <OptimalTableDemo /> },

  { path: 'organization', element: <Organization /> },

  { path: 'uploads', element: <FileUpload /> },
  { path: 'uploads/:uploadId', element: <UploadDetails /> },

  { path: 'video/:roomId', element: <VideoRoom /> },

  { path: 'notes', element: <UserNotesPage /> },

  { path: 'about/roles', element: <RoleDescriptions /> },

  { path: 'admin', element: <Administration /> },
];

function App() {
  let routes;

  if (!isTestMode) {
    useLoadPlugins();
    routes = usePluginRoutes(baseRoutes);
  } else {
    // For testing, we can use the base routes directly
    routes = baseRoutes;
  }

  const router = createBrowserRouter([
    {
      path: '/',
      element: <Home />,
      children: routes,
      errorElement: <ErrorPage />,
    },
  ]);

  return (
    <UserProvider>
      <NotificationProvider>
        <RouterProvider router={router} />
      </NotificationProvider>
    </UserProvider>
  );
}

export default App;
