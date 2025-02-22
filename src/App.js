import React, { useState, useEffect } from 'react';
import { Outlet, Link } from "react-router-dom";
import Joyride from 'react-joyride';
import { tourSteps } from './onboarding/tourSteps';
import './App.css';
import Calendar from 'react-calendar';
import PatientList from './components/PatientList';
import Patient from './components/Patient';

import API_URL from './env_vars'

function isSameDay (date1, date2) {
    return date1.getDate() === date2.getDate() && date1.getMonth() === date2.getMonth() && date1.getFullYear() === date2.getFullYear();
}

//const datesToAddContentTo = [tomorrow, in3Days, in5Days];
const datesToAddContentTo = [new Date(2025, 1, 1), new Date(2022, 2, 1), new Date(2022, 3, 1)];

function tileContent({ date, view }) {
  // Add class to tiles in month view only
  if (view === 'month') {
    // Check if a date React-Calendar wants to check is on the list of dates to add class to
    if (datesToAddContentTo.find(dDate => isSameDay(dDate, date))) {
      return 'My content';
    }
  }
}

function tileClassName({ date, view }) {
    const datesToAddClassTo = datesToAddContentTo;
  // Add class to tiles in month view only
  if (view === 'month') {
    // Check if a date React-Calendar wants to check is on the list of dates to add class to
    if (datesToAddClassTo.find(dDate => isSameDay(dDate, date))) {
      return 'myClassName';
    }
  }
}

import { createBrowserRouter, RouterProvider } from "react-router-dom";

function Home() {
    const [calendarValue, setCalendarValue] = useState(new Date());
    function onCalendarChange(nextValue) {setCalendarValue(nextValue);}

    const [currentTime, setCurrentTime] = useState(0);

    const [runTour, setRunTour] = useState(true);

    useEffect(() => {
        fetch(`${API_URL}/time`, {headers: {
            'Access-Control-Allow-Origin': 'http://127.0.0.1:3010',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
    }).then(res => res.json()).then(data => {
            setCurrentTime(data.time);
        });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                ... no changes in this part ...
                <p>The current time is {currentTime}.</p>
                <p><Link to="patients">Patients</Link></p>
                <p><Link to="about">About</Link></p>
                <p><Link to="contact">Contact</Link></p>
                <button className="sidebar-toggle-button">Toggle Sidebar</button>
                <button className="profile-button">Profile</button>
            </header>
            <Calendar onChange={onCalendarChange} value={calendarValue} tileContent={tileContent} tileClassName={tileClassName} />
            <main>
                {/* This is where the nested routes will render */}
                <Outlet />
            </main>
            <button className="create-new-button">Create New</button>
            <Joyride
                steps={tourSteps}
                continuous={true}      // let the user move from step to step seamlessly
                scrollToFirstStep={true}
                showProgress={true}   // display step count
                showSkipButton={true} // allow skipping
                run={runTour}         // start or stop the tour
                callback={(data) => {
                    const { status } = data;
                    if (status === 'finished' || status === 'skipped') {setRunTour(false);}
                }}
                styles={{
                    options: {zIndex: 10000}
                }}
            />
        </div>
    );
}

function About () {
    return (
        <div>
            <h1>About</h1>
            <p>This is the about page.</p>
        </div>
    );
}

function Contact () {
    return (
        <div>
        <h1>Contact</h1>
        <p>This is the contact page.</p>
        </div>
    );
}

function ErrorPage () {
    return (
        <div>
        <h1>404</h1>
        <p>Page not found.</p>
        </div>
    );
}

const router = createBrowserRouter([
    {
        path: "/",
        element: <Home />,
        children: [
            { path: "about", element: <About /> },
            { path: "contact", element: <Contact /> },
            { path: "patients", element: <PatientList /> },
            { path: "patients/:id", element: <Patient /> },
        ],
        errorElement: <ErrorPage />,
    },
]);

function App() {
    return <RouterProvider router={router} />;
}

export default App;
