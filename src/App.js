import React, { useState, useEffect } from 'react';
import { Outlet, Link } from "react-router-dom";
import './App.css';
import PatientList from './components/PatientList';
import Patient from './components/Patient';

import { createBrowserRouter, RouterProvider } from "react-router-dom";

function Home() {
    const [currentTime, setCurrentTime] = useState(0);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/time', {headers: {
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
            </header>
            <main>
                {/* This is where the nested routes will render */}
                <Outlet />
            </main>
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
