import React, { useEffect, useState } from 'react';
import { Link } from "react-router-dom";
import api from '../services/api';
import authService from '../services/auth';
import { useSignupPopup } from '../hooks/useSignupPopup';
import SignupPopup from './SignupPopup';

import API_URL from '../env_vars'

const PatientList = () => {
    const [patients, setPatients] = useState([]);
    const isAuthenticated = authService.isAuthenticated();
    const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

    useEffect(() => {
        //api.get('/patients')
        api.get(`${API_URL}/patients`)
            .then(response => {
                console.log(response.data)
                setPatients(response.data)
            })
            .catch(error => console.error(error));
    }, []);

    return (
        <>
            <div className="patient-list-container">
                <div className="patient-list-header">
                    <h1>Patient List</h1>
                    {!isAuthenticated && (
                        <div className="guest-notice">
                            <p>Sign up to create and manage patient records</p>
                            <button onClick={showSignupPopup} className="guest-action-button">
                                Get Started
                            </button>
                        </div>
                    )}
                </div>
                <ul className="patient-list">
                    {patients && patients.map((patient, index) => (
                        <li key={index} className="patient-item">
                            <Link to={`/patients/${patient.id}`} className="patient-link">
                                {patient.first_name} {patient.last_name}, {patient.age}
                            </Link>
                        </li>
                    ))}
                </ul>
            </div>
            <SignupPopup 
                isOpen={isPopupOpen} 
                onClose={hideSignupPopup}
            />
        </>
    );
};

export default PatientList;
