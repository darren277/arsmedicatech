import React from 'react';
import BarChart from '../components/BarChart';
import {useState, useEffect} from 'react';
import { Link } from "react-router-dom";

import API_URL from '../env_vars'

const Panel1 = () => {
    const [currentTime, setCurrentTime] = useState(0);

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
        <header className="App-header">
            ... no changes in this part ...
            <p>The current time is {currentTime}.</p>
            <p><Link to="patients">Patients</Link></p>
            <p><Link to="about">About</Link></p>
            <p><Link to="contact">Contact</Link></p>
            <button className="sidebar-toggle-button">Toggle Sidebar</button>
            <button className="profile-button">Profile</button>
        </header>
    )
}

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h2>Dashboard</h2>
      <div className="cards-grid">
        <div className="card">
            <Panel1 />
        </div>
        <div className="card"><BarChart /></div>
        <div className="card">Panel 3</div>
        <div className="card">Panel 4</div>
      </div>
    </div>
  );
};

export default Dashboard;
