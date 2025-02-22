import React, { useEffect, useState } from 'react';
import { Link } from "react-router-dom";
import api from '../services/api';

import API_URL from './env_vars'

const PatientList = () => {
    const [patients, setPatients] = useState([]);

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
        <div>
            {/* Render patient list: patients = [{"first_name": "John", "last_name": "Doe", "age": 45, "history": john_doe_history}, {"first_name": "Jane", "last_name": "Doe", "age": 35, "history": jane_doe_history}] */}
            <h1>Patient List</h1>
            <ul>
                {patients && patients.map((patient, index) => (
                    <li key={index}><Link to={`/patients/${patient.id}`}>{patient.first_name} {patient.last_name}, {patient.age}</Link></li>
                ))}
            </ul>
        </div>
    );
};

export default PatientList;
