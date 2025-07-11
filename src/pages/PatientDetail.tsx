import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { EncounterForm } from '../components/EncounterForm';
import { EncounterTable } from '../components/EncounterTable';
import { encounterAPI, patientAPI } from '../services/api';
import { EncounterType, PatientType } from '../types';

export function PatientDetail() {
  const { patientId } = useParams<{ patientId: string }>();
  const navigate = useNavigate();
  const [patient, setPatient] = useState<PatientType | null>(null);
  const [encounters, setEncounters] = useState<EncounterType[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [showEncounterForm, setShowEncounterForm] = useState(false);
  const [selectedEncounter, setSelectedEncounter] =
    useState<EncounterType | null>(null);

  useEffect(() => {
    if (patientId) {
      loadPatientData();
    }
  }, [patientId]);

  const loadPatientData = async () => {
    if (!patientId) return;

    setIsLoading(true);
    try {
      const [patientData, encountersData] = await Promise.all([
        patientAPI.getById(patientId),
        encounterAPI.getByPatient(patientId),
      ]);

      setPatient(patientData);
      setEncounters(encountersData);
    } catch (error) {
      console.error('Error loading patient data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleCreateEncounter = async (encounterData: any) => {
    if (!patientId) return;

    try {
      await encounterAPI.create(patientId, encounterData);
      setShowEncounterForm(false);
      loadPatientData();
    } catch (error) {
      console.error('Error creating encounter:', error);
    }
  };

  const handleUpdateEncounter = async (encounter: EncounterType) => {
    if (!encounter.note_id) return;

    try {
      await encounterAPI.update(encounter.note_id, encounter);
      setShowEncounterForm(false);
      loadPatientData();
    } catch (error) {
      console.error('Error updating encounter:', error);
    }
  };

  const handleDeleteEncounter = async (encounter: EncounterType) => {
    if (!encounter.note_id) return;

    if (window.confirm('Are you sure you want to delete this encounter?')) {
      try {
        await encounterAPI.delete(encounter.note_id);
        loadPatientData();
      } catch (error) {
        console.error('Error deleting encounter:', error);
      }
    }
  };

  const handleEncounterView = (encounter: EncounterType) => {
    navigate(`/encounters/${encounter.note_id}`);
  };

  const handleEncounterEdit = (encounter: EncounterType) => {
    // Navigate to the dedicated encounter edit page
    navigate(`/encounters/${encounter.note_id}/edit`);
  };

  const handleEncounterRowClick = (encounter: EncounterType) => {
    navigate(`/encounters/${encounter.note_id}`);
  };

  const handleNewEncounter = () => {
    // Navigate to the dedicated encounter creation page
    navigate(`/patients/${patientId}/encounters/new`);
  };

  if (isLoading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <p className="text-center">Loading patient details...</p>
      </div>
    );
  }

  if (!patient) {
    return (
      <div className="container mx-auto px-4 py-8">
        <p className="text-center text-red-600">Patient not found</p>
        <button
          onClick={() => navigate('/patients')}
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Back to Patients
        </button>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">
              {patient.first_name} {patient.last_name}
            </h1>
            <p className="text-gray-600">
              Patient ID: {patient.demographic_no}
            </p>
          </div>
          <div className="flex gap-2">
            <button
              onClick={handleNewEncounter}
              className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
            >
              New Encounter
            </button>
            <button
              onClick={() => navigate('/patients')}
              className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
            >
              Back to Patients
            </button>
          </div>
        </div>
      </div>

      {/* Patient Information */}
      <div className="bg-white shadow rounded-lg p-6 mb-8">
        <h2 className="text-xl font-semibold mb-4">Patient Information</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <p>
              <strong>First Name:</strong> {patient.first_name || '-'}
            </p>
            <p>
              <strong>Last Name:</strong> {patient.last_name || '-'}
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
          </div>
          <div>
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
      </div>

      {/* Encounters Section */}
      <div className="bg-white shadow rounded-lg p-6">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-semibold">Encounters</h2>
          <button
            onClick={handleNewEncounter}
            className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
          >
            Add New Encounter
          </button>
        </div>

        <EncounterTable
          encounters={encounters}
          onView={handleEncounterView}
          onEdit={handleEncounterEdit}
          onDelete={handleDeleteEncounter}
          onRowClick={handleEncounterRowClick}
        />
      </div>

      {/* Encounter Form Modal - keeping for backward compatibility */}
      {showEncounterForm && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto">
            <EncounterForm
              encounter={selectedEncounter}
              patientId={patientId}
              onSubmit={
                selectedEncounter
                  ? handleUpdateEncounter
                  : handleCreateEncounter
              }
              onCancel={() => {
                setShowEncounterForm(false);
                setSelectedEncounter(null);
              }}
              isLoading={false}
            />
          </div>
        </div>
      )}
    </div>
  );
}
