import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { EncounterForm } from '../components/EncounterForm';
import { encounterAPI, patientAPI } from '../services/api';
import { EncounterType, PatientType } from '../types';

export function EncounterFormPage() {
  const navigate = useNavigate();
  const { encounterId, patientId } = useParams<{
    encounterId?: string;
    patientId?: string;
  }>();

  const [encounter, setEncounter] = useState<EncounterType | null>(null);
  const [patient, setPatient] = useState<PatientType | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isInitializing, setIsInitializing] = useState(true);

  useEffect(() => {
    const initializeData = async () => {
      try {
        // If editing an existing encounter, load it
        if (encounterId) {
          const encounterData = await encounterAPI.getById(encounterId);
          setEncounter(encounterData);

          // If encounter has patient data, use it
          if (encounterData.patient) {
            setPatient(encounterData.patient);
          }
        }

        // If creating a new encounter and patientId is provided, load patient
        if (!encounterId && patientId) {
          const patientData = await patientAPI.getById(patientId);
          setPatient(patientData);
        }
      } catch (error) {
        console.error('Error initializing encounter form:', error);
        // Handle error - could show a toast notification here
      } finally {
        setIsInitializing(false);
      }
    };

    initializeData();
  }, [encounterId, patientId]);

  const handleSubmit = async (encounterData: any) => {
    setIsLoading(true);
    try {
      if (encounterId) {
        // Update existing encounter
        await encounterAPI.update(encounterId, encounterData);
      } else {
        // Create new encounter
        const targetPatientId = patientId || patient?.demographic_no;
        if (!targetPatientId) {
          throw new Error('Patient ID is required to create an encounter');
        }
        await encounterAPI.create(targetPatientId, encounterData);
      }

      // Navigate back to the appropriate page
      if (patient?.demographic_no) {
        navigate(`/patients/${patient.demographic_no}`);
      } else {
        navigate('/patients');
      }
    } catch (error) {
      console.error('Error saving encounter:', error);
      // Handle error - could show a toast notification here
    } finally {
      setIsLoading(false);
    }
  };

  const handleCancel = () => {
    // Navigate back to the appropriate page
    if (patient?.demographic_no) {
      navigate(`/patients/${patient.demographic_no}`);
    } else {
      navigate('/patients');
    }
  };

  if (isInitializing) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="flex items-center justify-center min-h-64">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
            <p className="text-gray-600">Loading encounter form...</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">
              {encounter ? 'Edit Encounter' : 'New Encounter'}
            </h1>
            {patient && (
              <p className="text-gray-600 mt-2">
                Patient: {patient.first_name} {patient.last_name} (ID:{' '}
                {patient.demographic_no})
              </p>
            )}
          </div>
          <button
            onClick={handleCancel}
            className="px-4 py-2 text-gray-600 bg-gray-100 rounded-md hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-500"
          >
            ← Back
          </button>
        </div>
      </div>

      {/* Encounter Form */}
      <EncounterForm
        encounter={encounter}
        patientId={patientId || patient?.demographic_no}
        onSubmit={handleSubmit}
        onCancel={handleCancel}
        isLoading={isLoading}
      />
    </div>
  );
}
