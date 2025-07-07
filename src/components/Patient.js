import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';
import authService from '../services/auth';
import { useSignupPopup } from '../hooks/useSignupPopup';
import SignupPopup from './SignupPopup';

import API_URL from '../env_vars'

const Patient = () => {
    const { id } = useParams();
    const [patient, setPatient] = useState({ history: [] });
    const isAuthenticated = authService.isAuthenticated();
    const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

    useEffect(() => {
        //api.get('/patients')
        api.get(`${API_URL}/patients/${id}`)
            .then(response => {
                console.log('PATIENT DATA:', response.data)
                setPatient(response.data)
            })
            .catch(error => console.error(error));
    }, []);

    return (
        <>
            <div className="patient-detail-container">
                {patient.first_name ? (
                    <>
                        <div className="patient-detail-header">
                            <h1>Patient: {patient.first_name} {patient.last_name}</h1>
                            {!isAuthenticated && (
                                <div className="guest-notice">
                                    <p>Sign up to edit patient records and add notes</p>
                                    <button onClick={showSignupPopup} className="guest-action-button">
                                        Get Started
                                    </button>
                                </div>
                            )}
                        </div>
                        <div className="patient-history">
                            <h2>Medical History</h2>
                            <ul className="history-list">
                                {patient && patient?.history.length && patient.history.map((event, index) => (
                                    <li key={index} className="history-item">
                                        <span className="history-date">{event.date}:</span> {event.note}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    </>
                ) : (
                    <h1>Loading patient data...</h1>
                )}
            </div>
            <SignupPopup 
                isOpen={isPopupOpen} 
                onClose={hideSignupPopup}
            />
        </>
    );
};

export default Patient;
