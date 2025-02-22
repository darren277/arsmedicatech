import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';

import API_URL from '../env_vars'

const Patient = () => {
    const { id } = useParams();
    const [patient, setPatient] = useState({ history: [] });

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
        <div>
            {/* Render patient details (john_doe_history = [
    {"date": "2021-01-01", "note": "Patient has a fever."},
    {"date": "2021-01-02", "note": "Patient has a cough."},
    {"date": "2021-01-03", "note": "Patient has a headache."}
]) */}
        {patient.first_name ? (
            <>
                <h1>Name: {patient.first_name} {patient.last_name}</h1>
                <ul>
                    {patient && patient?.history.length && patient.history.map((event, index) => (
                        <li key={index}>{event.date}: {event.note}</li>
                    ))}
                </ul>
            </>
        ) : (
            <h1>Loading patient data...</h1>
        )}
        </div>
    );
};

export default Patient;
