import React, { useEffect, useState } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { patientAPI } from '../services/api';
import authService from '../services/auth';
import { useSignupPopup } from '../hooks/useSignupPopup';
import SignupPopup from './SignupPopup';

import API_URL from '../env_vars'

const Patient = () => {
    const { id } = useParams();
    const [patient, setPatient] = useState({ history: [] });
    const isAuthenticated = authService.isAuthenticated();
    const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();
    const navigate = useNavigate();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        loadPatient();
    }, [id]);

    const loadPatient = async () => {
        try {
            setLoading(true);
            const response = await patientAPI.getById(id);
            setPatient(response.data);
        } catch (err) {
            setError('Failed to load patient data');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleEdit = () => {
        navigate(`/patients/${id}/edit`);
    };

    const handleDelete = async () => {
        if (window.confirm(`Are you sure you want to delete ${patient.first_name} ${patient.last_name}?`)) {
            try {
                await patientAPI.delete(id);
                navigate('/patients');
            } catch (err) {
                setError('Failed to delete patient');
                console.error(err);
            }
        }
    };

    if (loading) {
        return <div className="flex justify-center items-center h-64">Loading patient data...</div>;
    }

    if (error) {
        return (
            <div className="max-w-4xl mx-auto p-6">
                <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                    {error}
                </div>
                <Link to="/patients" className="text-blue-600 hover:text-blue-900">
                    ← Back to Patient List
                </Link>
            </div>
        );
    }

    if (!patient) {
        return (
            <div className="max-w-4xl mx-auto p-6">
                <div className="text-center">
                    <h1 className="text-2xl font-bold mb-4">Patient Not Found</h1>
                    <Link to="/patients" className="text-blue-600 hover:text-blue-900">
                        ← Back to Patient List
                    </Link>
                </div>
            </div>
        );
    }

    const formatDate = (dateString) => {
        if (!dateString) return '-';
        return new Date(dateString).toLocaleDateString();
    };

    const formatLocation = (location) => {
        if (!location || !Array.isArray(location)) return '-';
        return location.filter(Boolean).join(', ') || '-';
    };

    return (
      <>
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
        <div className="max-w-4xl mx-auto p-6">
            <div className="flex justify-between items-center mb-6">
                <div>
                    <Link to="/patients" className="text-blue-600 hover:text-blue-900 mb-2 inline-block">
                        ← Back to Patient List
                    </Link>
                    <h1 className="text-3xl font-bold">
                        {patient.first_name} {patient.last_name}
                    </h1>
                    <p className="text-gray-600">Patient ID: {patient.demographic_no}</p>
                </div>
                <div className="flex space-x-2">
                    <button
                        onClick={handleEdit}
                        className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                    >
                        Edit Patient
                    </button>
                    <button
                        onClick={handleDelete}
                        className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700"
                    >
                        Delete Patient
                    </button>
                </div>
            </div>

            <div className="bg-white shadow-md rounded-lg overflow-hidden">
                <div className="px-6 py-4 border-b border-gray-200">
                    <h2 className="text-xl font-semibold">Patient Information</h2>
                </div>
                
                <div className="p-6">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h3 className="text-lg font-medium mb-4">Personal Details</h3>
                            <dl className="space-y-3">
                                <div>
                                    <dt className="text-sm font-medium text-gray-500">Full Name</dt>
                                    <dd className="text-sm text-gray-900">{patient.first_name} {patient.last_name}</dd>
                                </div>
                                <div>
                                    <dt className="text-sm font-medium text-gray-500">Date of Birth</dt>
                                    <dd className="text-sm text-gray-900">{formatDate(patient.date_of_birth)}</dd>
                                </div>
                                <div>
                                    <dt className="text-sm font-medium text-gray-500">Sex</dt>
                                    <dd className="text-sm text-gray-900">
                                        {patient.sex === 'M' ? 'Male' : patient.sex === 'F' ? 'Female' : patient.sex === 'O' ? 'Other' : '-'}
                                    </dd>
                                </div>
                            </dl>
                        </div>

                        <div>
                            <h3 className="text-lg font-medium mb-4">Contact Information</h3>
                            <dl className="space-y-3">
                                <div>
                                    <dt className="text-sm font-medium text-gray-500">Phone</dt>
                                    <dd className="text-sm text-gray-900">{patient.phone || '-'}</dd>
                                </div>
                                <div>
                                    <dt className="text-sm font-medium text-gray-500">Email</dt>
                                    <dd className="text-sm text-gray-900">{patient.email || '-'}</dd>
                                </div>
                                <div>
                                    <dt className="text-sm font-medium text-gray-500">Address</dt>
                                    <dd className="text-sm text-gray-900">{formatLocation(patient.location)}</dd>
                                </div>
                            </dl>
                        </div>
                    </div>

                    {/* Placeholder for future features */}
                    <div className="mt-8 pt-6 border-t border-gray-200">
                        <h3 className="text-lg font-medium mb-4">Medical History</h3>
                        <div className="bg-gray-50 p-4 rounded-md">
                            <p className="text-gray-600 text-sm">
                                Medical history and encounter information will be displayed here.
                                This feature is coming soon.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </>
    );
};

export default Patient;
