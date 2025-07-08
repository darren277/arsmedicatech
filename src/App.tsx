import { useState } from 'react';
import Joyride from 'react-joyride';
import { Outlet } from 'react-router-dom';
import './App.css';
import Patient from './components/Patient';
import PatientForm from './components/PatientForm';
import PatientList from './components/PatientList';
import { PatientTable } from './components/PatientTable';
import { usePatientSearch } from './hooks/usePatientSearch';
import { tourSteps } from './onboarding/tourSteps';

import Sidebar from './components/Sidebar';
import Topbar from './components/Topbar';

import Dashboard from './pages/Dashboard';
import Messages from './pages/Messages';
import Schedule from './pages/Schedule';

import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { UserProvider } from './components/UserContext';

function Home() {
  console.log('Home component rendered');

  const [runTour, setRunTour] = useState(true);

  const { query, setQuery, results, loading } = usePatientSearch();

  return (
    <div className="App app-container">
      <Sidebar />
      <div className="main-container">
        <Topbar
          query={query}
          onQueryChange={setQuery}
          results={results}
          loading={loading}
        />

        <PatientTable rows={results} />

        <div className="main-content">
          <main>
            {/* This is where the nested routes will render */}
            <Outlet />
          </main>
          <button className="create-new-button">Create New</button>
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

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: 'about', element: <About /> },
      { path: 'contact', element: <Contact /> },
      { path: 'patients', element: <PatientList /> },
      { path: 'patients/new', element: <PatientForm /> },
      { path: 'patients/:id', element: <Patient /> },
      { path: 'patients/:id/edit', element: <PatientForm /> },
      { path: 'schedule', element: <Schedule /> },
      { path: 'messages', element: <Messages /> },
    ],
    errorElement: <ErrorPage />,
  },
]);

function App() {
  return (
    <UserProvider>
      <RouterProvider router={router} />
    </UserProvider>
  );
}

export default App;
