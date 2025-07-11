import { useEffect, useState } from 'react';
import { useSignupPopup } from '../hooks/useSignupPopup';
import authService from '../services/auth';
import { PatientType } from '../types';
import SignupPopup from './SignupPopup';

import { Link, useNavigate } from 'react-router-dom';
import { patientAPI } from '../services/api';

const PatientList = () => {
  const [patients, setPatients] = useState<PatientType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const isAuthenticated = authService.isAuthenticated();
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

  useEffect(() => {
    loadPatients();
  }, []);

  const loadPatients = async () => {
    try {
      setLoading(true);
      const response = await patientAPI.getAll();
      // Handle both response structures
      const patientsData = response.data || response;
      setPatients(patientsData || []);
    } catch (err) {
      setError('Failed to load patients');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (
    patientId: string,
    patientName: string
  ): Promise<void> => {
    if (window.confirm(`Are you sure you want to delete ${patientName}?`)) {
      try {
        await patientAPI.delete(patientId);
        loadPatients(); // Reload the list
      } catch (err) {
        setError('Failed to delete patient');
        console.error(err);
      }
    }
  };

  const handleEdit = (patientId: string): void => {
    navigate(`/patients/${patientId}/edit`);
  };

  const handleAddNew = (): void => {
    navigate('/patients/new');
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        Loading patients...
      </div>
    );
  }

  return (
    <>
      <div className="max-w-6xl mx-auto p-6">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold">Patient List</h1>
          {isAuthenticated ? (
            <button
              onClick={handleAddNew}
              className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
            >
              Add New Patient
            </button>
          ) : (
            <div className="guest-notice">
              <p>Sign up to create and manage patient records</p>
              <button onClick={showSignupPopup} className="guest-action-button">
                Get Started
              </button>
            </div>
          )}
        </div>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}

        {patients && patients.length > 0 ? (
          <div className="bg-white shadow-md rounded-lg overflow-hidden">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Name
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    ID
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Date of Birth
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Phone
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Email
                  </th>
                  {isAuthenticated && (
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Actions
                    </th>
                  )}
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {patients.map(patient => (
                  <tr key={patient.demographic_no} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap">
                      <Link
                        to={`/patients/${patient.demographic_no}`}
                        className="text-blue-600 hover:text-blue-900 font-medium"
                      >
                        {patient.first_name} {patient.last_name}
                      </Link>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                      {patient.demographic_no}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                      {patient.date_of_birth
                        ? new Date(patient.date_of_birth).toLocaleDateString()
                        : '-'}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                      {patient.phone || '-'}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                      {patient.email || '-'}
                    </td>
                    {isAuthenticated && (
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                        <div className="flex space-x-2">
                          <button
                            onClick={() =>
                              patient.demographic_no &&
                              handleEdit(patient.demographic_no)
                            }
                            className="text-indigo-600 hover:text-indigo-900"
                          >
                            Edit
                          </button>
                          <button
                            onClick={() => {
                              if (patient.demographic_no) {
                                handleDelete(
                                  patient.demographic_no,
                                  `${patient.first_name} ${patient.last_name}`
                                );
                              }
                            }}
                            className="text-red-600 hover:text-red-900"
                          >
                            Delete
                          </button>
                        </div>
                      </td>
                    )}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="text-center py-8">
            <p className="text-gray-500 mb-4">No patients found</p>
            {isAuthenticated ? (
              <button
                onClick={handleAddNew}
                className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
              >
                Add Your First Patient
              </button>
            ) : (
              <button
                onClick={showSignupPopup}
                className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
              >
                Sign Up to Add Patients
              </button>
            )}
          </div>
        )}
      </div>
      <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />
    </>
  );
};

export default PatientList;
