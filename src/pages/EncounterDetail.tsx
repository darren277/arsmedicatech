import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { encounterAPI } from '../services/api';
import { EncounterType, PatientType, SOAPNotesType } from '../types';

export function EncounterDetail() {
  const { encounterId } = useParams<{ encounterId: string }>();
  const navigate = useNavigate();
  const [encounter, setEncounter] = useState<EncounterType | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (encounterId) {
      loadEncounterData();
    }
  }, [encounterId]);

  const loadEncounterData = async () => {
    if (!encounterId) return;

    setIsLoading(true);
    try {
      const encounterData = await encounterAPI.getById(encounterId);
      setEncounter(encounterData);
    } catch (error) {
      console.error('Error loading encounter data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const renderSOAPNotes = (soapNotes: SOAPNotesType) => {
    return (
      <div className="space-y-4">
        <div>
          <h4 className="font-semibold text-blue-600">Subjective</h4>
          <p className="text-gray-700 bg-gray-50 p-3 rounded">
            {soapNotes.subjective || 'No subjective notes'}
          </p>
        </div>
        <div>
          <h4 className="font-semibold text-green-600">Objective</h4>
          <p className="text-gray-700 bg-gray-50 p-3 rounded">
            {soapNotes.objective || 'No objective notes'}
          </p>
        </div>
        <div>
          <h4 className="font-semibold text-yellow-600">Assessment</h4>
          <p className="text-gray-700 bg-gray-50 p-3 rounded">
            {soapNotes.assessment || 'No assessment notes'}
          </p>
        </div>
        <div>
          <h4 className="font-semibold text-red-600">Plan</h4>
          <p className="text-gray-700 bg-gray-50 p-3 rounded">
            {soapNotes.plan || 'No plan notes'}
          </p>
        </div>
      </div>
    );
  };

  const renderNoteText = (noteText: any) => {
    if (typeof noteText === 'object' && noteText !== null) {
      return renderSOAPNotes(noteText as SOAPNotesType);
    }
    return (
      <div>
        <h4 className="font-semibold text-gray-600 mb-2">Notes</h4>
        <p className="text-gray-700 bg-gray-50 p-3 rounded whitespace-pre-wrap">
          {noteText || 'No notes available'}
        </p>
      </div>
    );
  };

  if (isLoading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <p className="text-center">Loading encounter details...</p>
      </div>
    );
  }

  if (!encounter) {
    return (
      <div className="container mx-auto px-4 py-8">
        <p className="text-center text-red-600">Encounter not found</p>
        <button
          onClick={() => navigate('/patients')}
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Back to Patients
        </button>
      </div>
    );
  }

  const patient = encounter.patient as PatientType;

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">
              Encounter Details
            </h1>
            <p className="text-gray-600">Note ID: {encounter.note_id}</p>
            {patient && (
              <p className="text-gray-600">
                Patient: {patient.first_name} {patient.last_name} (ID:{' '}
                {patient.demographic_no})
              </p>
            )}
          </div>
          <div className="flex space-x-2">
            {patient && (
              <button
                onClick={() => navigate(`/patients/${patient.demographic_no}`)}
                className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
              >
                View Patient
              </button>
            )}
            <button
              onClick={() => navigate('/patients')}
              className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
            >
              Back to Patients
            </button>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Encounter Information */}
        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Encounter Information</h2>
          <div className="space-y-3">
            <p>
              <strong>Note ID:</strong> {encounter.note_id || '-'}
            </p>
            <p>
              <strong>Visit Date:</strong>{' '}
              {encounter.date_created
                ? new Date(encounter.date_created).toLocaleDateString()
                : '-'}
            </p>
            <p>
              <strong>Provider:</strong> {encounter.provider_id || '-'}
            </p>
            <p>
              <strong>Status:</strong> {encounter.status || '-'}
            </p>
            {encounter.diagnostic_codes &&
              encounter.diagnostic_codes.length > 0 && (
                <div>
                  <strong>Diagnostic Codes:</strong>
                  <div className="mt-1">
                    {encounter.diagnostic_codes.map((code, index) => (
                      <span
                        key={index}
                        className="inline-block bg-blue-100 text-blue-800 px-2 py-1 rounded text-sm mr-2 mb-1"
                      >
                        {code}
                      </span>
                    ))}
                  </div>
                </div>
              )}
          </div>
        </div>

        {/* Patient Information */}
        {patient && (
          <div className="bg-white shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold mb-4">Patient Information</h2>
            <div className="space-y-3">
              <p>
                <strong>Name:</strong> {patient.first_name} {patient.last_name}
              </p>
              <p>
                <strong>ID:</strong> {patient.demographic_no}
              </p>
              <p>
                <strong>Date of Birth:</strong>{' '}
                {patient.date_of_birth
                  ? new Date(patient.date_of_birth).toLocaleDateString()
                  : '-'}
              </p>
              <p>
                <strong>Sex:</strong> {patient.sex || '-'}
              </p>
              <p>
                <strong>Phone:</strong> {patient.phone || '-'}
              </p>
              <p>
                <strong>Email:</strong> {patient.email || '-'}
              </p>
              <p>
                <strong>Address:</strong>{' '}
                {patient.location ? patient.location.join(', ') : '-'}
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Notes Section */}
      <div className="mt-8 bg-white shadow rounded-lg p-6">
        <h2 className="text-xl font-semibold mb-4">Clinical Notes</h2>
        {renderNoteText(encounter.note_text)}
      </div>

      {/* Action Buttons */}
      <div className="mt-8 flex justify-center space-x-4">
        <button
          onClick={() => navigate(`/encounters/${encounter.note_id}/edit`)}
          className="px-6 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600"
        >
          Edit Encounter
        </button>
        {patient && (
          <button
            onClick={() => navigate(`/patients/${patient.demographic_no}`)}
            className="px-6 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            View All Encounters
          </button>
        )}
      </div>
    </div>
  );
}
