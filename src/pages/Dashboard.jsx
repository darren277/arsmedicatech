import React from 'react';
import BarChart from '../components/BarChart';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h2>Dashboard</h2>
      <div className="cards-grid">
        <div className="card">Panel 1</div>
        <BarChart />
        <div className="card">Panel 2</div>
        <div className="card">Panel 3</div>
        <div className="card">Panel 4</div>
      </div>
    </div>
  );
};

export default Dashboard;
