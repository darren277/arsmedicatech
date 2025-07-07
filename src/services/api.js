import axios from 'axios';

import API_URL from '../env_vars'

const api = axios.create({
    //baseURL: 'http://127.0.0.1:5000',
    //baseURL: process.env.REACT_APP_API_URL,
    baseURL: API_URL
});

// Patient CRUD operations
export const patientAPI = {
    // Get all patients
    getAll: () => api.get('/patients'),
    
    // Get a specific patient
    getById: (id) => api.get(`/patients/${id}`),
    
    // Create a new patient
    create: (patientData) => api.post('/patients', patientData),
    
    // Update a patient
    update: (id, patientData) => api.put(`/patients/${id}`, patientData),
    
    // Delete a patient
    delete: (id) => api.delete(`/patients/${id}`),
    
    // Search patients
    search: (query) => api.get(`/patients/search?q=${encodeURIComponent(query)}`)
};

export default api;
