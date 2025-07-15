import React, { useEffect, useState } from 'react';
import { organizationAPI } from '../services/api';

interface Clinic {
  id: string;
  name: string;
  address: {
    street: string;
    city: string;
    state: string;
    zip: string;
    country: string;
  };
  location: {
    type: string;
    coordinates: [number, number];
  };
}

interface ClinicListProps {
  organizationId: string;
  onUpdate?: () => void;
}

const ClinicList: React.FC<ClinicListProps> = ({
  organizationId,
  onUpdate,
}) => {
  const [clinics, setClinics] = useState<Clinic[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [newClinicId, setNewClinicId] = useState('');
  const [addingClinic, setAddingClinic] = useState(false);

  useEffect(() => {
    loadClinics();
  }, [organizationId]);

  const loadClinics = async () => {
    try {
      setLoading(true);
      const response = await organizationAPI.getClinics(organizationId);
      if (response && response.clinics) {
        setClinics(response.clinics);
      } else {
        setClinics([]);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to load clinics');
    } finally {
      setLoading(false);
    }
  };

  const handleAddClinic = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newClinicId.trim()) return;

    try {
      setAddingClinic(true);
      await organizationAPI.addClinic(organizationId, newClinicId.trim());
      setNewClinicId('');
      await loadClinics();
      if (onUpdate) onUpdate();
    } catch (err: any) {
      setError(err.message || 'Failed to add clinic');
    } finally {
      setAddingClinic(false);
    }
  };

  const handleRemoveClinic = async (clinicId: string) => {
    if (
      !confirm(
        'Are you sure you want to remove this clinic from the organization?'
      )
    ) {
      return;
    }

    try {
      await organizationAPI.removeClinic(organizationId, clinicId);
      await loadClinics();
      if (onUpdate) onUpdate();
    } catch (err: any) {
      setError(err.message || 'Failed to remove clinic');
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center py-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-medium text-gray-900">Clinics</h3>
        <span className="text-sm text-gray-500">
          {clinics.length} clinic(s)
        </span>
      </div>

      {/* Add Clinic Form */}
      <form onSubmit={handleAddClinic} className="flex gap-2">
        <input
          type="text"
          value={newClinicId}
          onChange={e => setNewClinicId(e.target.value)}
          placeholder="Enter clinic ID to add"
          className="flex-1 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        />
        <button
          type="submit"
          disabled={addingClinic || !newClinicId.trim()}
          className="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {addingClinic ? 'Adding...' : 'Add Clinic'}
        </button>
      </form>

      {/* Error Message */}
      {error && (
        <div className="rounded-md bg-red-50 p-4">
          <div className="flex">
            <div className="flex-shrink-0">
              <svg
                className="h-5 w-5 text-red-400"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clipRule="evenodd"
                />
              </svg>
            </div>
            <div className="ml-3">
              <p className="text-sm text-red-800">{error}</p>
            </div>
          </div>
        </div>
      )}

      {/* Clinics List */}
      {clinics.length === 0 ? (
        <div className="text-center py-8">
          <svg
            className="mx-auto h-12 w-12 text-gray-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
            />
          </svg>
          <h3 className="mt-2 text-sm font-medium text-gray-900">No clinics</h3>
          <p className="mt-1 text-sm text-gray-500">
            Get started by adding a clinic to this organization.
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          {clinics.map(clinic => (
            <div
              key={clinic.id}
              className="bg-white border border-gray-200 rounded-lg p-4 shadow-sm"
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <h4 className="text-lg font-medium text-gray-900">
                    {clinic.name}
                  </h4>
                  <p className="text-sm text-gray-600 mt-1">
                    {clinic.address.street}, {clinic.address.city},{' '}
                    {clinic.address.state} {clinic.address.zip}
                  </p>
                  <p className="text-sm text-gray-500 mt-1">
                    {clinic.address.country}
                  </p>
                  {clinic.location && (
                    <p className="text-xs text-gray-400 mt-1">
                      Location: {clinic.location.coordinates[1].toFixed(4)},{' '}
                      {clinic.location.coordinates[0].toFixed(4)}
                    </p>
                  )}
                </div>
                <button
                  onClick={() => handleRemoveClinic(clinic.id)}
                  className="ml-4 inline-flex items-center px-3 py-1 border border-red-300 rounded-md text-sm font-medium text-red-700 bg-white hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                >
                  Remove
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ClinicList;
