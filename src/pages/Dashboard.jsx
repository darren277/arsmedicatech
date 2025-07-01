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

const DashboardOld = () => {
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

const dashboardData = {
    totalPatients: '1,083',
    totalIncome: '723.43',
    appointments: '324',
    reports: '1,083'
};

const Dashboard = () => {
    return (
        <div className="dashboard">
            <div className="dashboard-header">
                <h1>Dashboard</h1>
            </div>
            <div className="dashboard-grid">
                <div className="card stats-card">
                    <div className="card-title">Total Patients</div>
                    <h2>{dashboardData.totalPatients}</h2>
                    <p>+2.7%</p>
                </div>
                <div className="card stats-card">
                    <div className="card-title">Total Income</div>
                    <h2>${dashboardData.totalIncome}</h2>
                    <p>+2.7%</p>
                </div>
                <div className="card stats-card">
                    <div className="card-title">Appointments</div>
                    <h2>{dashboardData.appointments}</h2>
                    <p>+2.7%</p>
                </div>
                <div className="card stats-card">
                    <div className="card-title">Reports</div>
                    <h2>{dashboardData.reports}</h2>
                    <p>+2.7%</p>
                </div>

                <div className="card appointments-card">
                    <div className="card-title">Appointments</div>
                    {/* This would be a list rendered from data */}
                </div>

                <div className="card activity-card">
                    <div className="card-title">Recent Activity</div>
                    {/* This would be a list rendered from data */}
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
