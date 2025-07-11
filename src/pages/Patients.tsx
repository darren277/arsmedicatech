import { useEffect, useState } from 'react';
import { EncounterForm } from '../components/EncounterForm';
import { EncounterTable } from '../components/EncounterTable';
import { PatientFormModal } from '../components/PatientFormModal';
import { PatientTable } from '../components/PatientTable';
import { encounterAPI, patientAPI } from '../services/api';
import { EncounterType, PatientType } from '../types';

export function Patients() {
  const [patients, setPatients] = useState<PatientType[]>([]);
  const [encounters, setEncounters] = useState<EncounterType[]>([]);
  const [selectedPatient, setSelectedPatient] = useState<PatientType | null>(
    null
  );
  const [selectedEncounter, setSelectedEncounter] =
    useState<EncounterType | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [showPatientForm, setShowPatientForm] = useState(false);
  const [showEncounterForm, setShowEncounterForm] = useState(false);
  const [activeTab, setActiveTab] = useState<'patients' | 'encounters'>(
    'patients'
  );

  // Load patients on component mount
  useEffect(() => {
    loadPatients();
  }, []);

  // Load encounters when a patient is selected
  useEffect(() => {
    if (selectedPatient?.demographic_no) {
      loadPatientEncounters(selectedPatient.demographic_no);
    }
  }, [selectedPatient]);

  const loadPatients = async () => {
    setIsLoading(true);
    try {
      const data = await patientAPI.getAll();
      setPatients(data);
    } catch (error) {
      console.error('Error loading patients:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const loadPatientEncounters = async (patientId: string) => {
    setIsLoading(true);
    try {
      const data = await encounterAPI.getByPatient(patientId);
      setEncounters(data);
    } catch (error) {
      console.error('Error loading patient encounters:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleCreatePatient = async (patientData: any) => {
    try {
      await patientAPI.create(patientData);
      setShowPatientForm(false);
      loadPatients();
    } catch (error) {
      console.error('Error creating patient:', error);
    }
  };

  const handleUpdatePatient = async (patient: PatientType) => {
    if (!patient.demographic_no) return;

    try {
      await patientAPI.update(patient.demographic_no, patient);
      setShowPatientForm(false);
      loadPatients();
    } catch (error) {
      console.error('Error updating patient:', error);
    }
  };

  const handleDeletePatient = async (patient: PatientType) => {
    if (!patient.demographic_no) return;

    if (window.confirm('Are you sure you want to delete this patient?')) {
      try {
        await patientAPI.delete(patient.demographic_no);
        loadPatients();
        if (selectedPatient?.demographic_no === patient.demographic_no) {
          setSelectedPatient(null);
          setEncounters([]);
        }
      } catch (error) {
        console.error('Error deleting patient:', error);
      }
    }
  };

  const handleCreateEncounter = async (encounterData: any) => {
    if (!selectedPatient?.demographic_no) return;

    try {
      await encounterAPI.create(selectedPatient.demographic_no, encounterData);
      setShowEncounterForm(false);
      loadPatientEncounters(selectedPatient.demographic_no);
    } catch (error) {
      console.error('Error creating encounter:', error);
    }
  };

  const handleUpdateEncounter = async (encounter: EncounterType) => {
    if (!encounter.note_id) return;

    try {
      await encounterAPI.update(encounter.note_id, encounter);
      setShowEncounterForm(false);
      if (selectedPatient?.demographic_no) {
        loadPatientEncounters(selectedPatient.demographic_no);
      }
    } catch (error) {
      console.error('Error updating encounter:', error);
    }
  };

  const handleDeleteEncounter = async (encounter: EncounterType) => {
    if (!encounter.note_id) return;

    if (window.confirm('Are you sure you want to delete this encounter?')) {
      try {
        await encounterAPI.delete(encounter.note_id);
        if (selectedPatient?.demographic_no) {
          loadPatientEncounters(selectedPatient.demographic_no);
        }
      } catch (error) {
        console.error('Error deleting encounter:', error);
      }
    }
  };

  const handlePatientView = (patient: PatientType) => {
    setSelectedPatient(patient);
    setActiveTab('encounters');
  };

  const handlePatientEdit = (patient: PatientType) => {
    setSelectedPatient(patient);
    setShowPatientForm(true);
  };

  const handleEncounterView = (encounter: EncounterType) => {
    setSelectedEncounter(encounter);
    setShowEncounterForm(true);
  };

  const handleEncounterEdit = (encounter: EncounterType) => {
    setSelectedEncounter(encounter);
    setShowEncounterForm(true);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Patient Management
        </h1>

        {/* Tab Navigation */}
        <div className="border-b border-gray-200 mb-6">
          <nav className="-mb-px flex space-x-8">
            <button
              onClick={() => setActiveTab('patients')}
              className={`py-2 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'patients'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              Patients
            </button>
            <button
              onClick={() => setActiveTab('encounters')}
              disabled={!selectedPatient}
              className={`py-2 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'encounters'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              } ${!selectedPatient ? 'opacity-50 cursor-not-allowed' : ''}`}
            >
              Encounters{' '}
              {selectedPatient &&
                `(${selectedPatient.first_name} ${selectedPatient.last_name})`}
            </button>
          </nav>
        </div>

        {/* Action Buttons */}
        <div className="flex justify-between items-center mb-6">
          {activeTab === 'patients' && (
            <button
              onClick={() => {
                setSelectedPatient(null);
                setShowPatientForm(true);
              }}
              className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
            >
              Add New Patient
            </button>
          )}

          {activeTab === 'encounters' && selectedPatient && (
            <button
              onClick={() => {
                setSelectedEncounter(null);
                setShowEncounterForm(true);
              }}
              className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600"
            >
              Add New Encounter
            </button>
          )}
        </div>
      </div>

      {/* Content */}
      {activeTab === 'patients' && (
        <div>
          <PatientTable
            patients={patients}
            isLoading={isLoading}
            onView={handlePatientView}
            onEdit={handlePatientEdit}
            onDelete={handleDeletePatient}
          />
        </div>
      )}

      {activeTab === 'encounters' && selectedPatient && (
        <div>
          <div className="mb-4 p-4 bg-blue-50 rounded-lg">
            <h3 className="text-lg font-semibold text-blue-900">
              Encounters for {selectedPatient.first_name}{' '}
              {selectedPatient.last_name}
            </h3>
            <p className="text-blue-700">
              Patient ID: {selectedPatient.demographic_no}
            </p>
          </div>

          <EncounterTable
            encounters={encounters}
            isLoading={isLoading}
            onView={handleEncounterView}
            onEdit={handleEncounterEdit}
            onDelete={handleDeleteEncounter}
          />
        </div>
      )}

      {/* Modals */}
      {showPatientForm && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
            <PatientFormModal
              patient={selectedPatient}
              onSubmit={
                selectedPatient ? handleUpdatePatient : handleCreatePatient
              }
              onCancel={() => {
                setShowPatientForm(false);
                setSelectedPatient(null);
              }}
              isLoading={isLoading}
            />
          </div>
        </div>
      )}

      {showEncounterForm && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto">
            <EncounterForm
              encounter={selectedEncounter}
              patientId={selectedPatient?.demographic_no}
              onSubmit={
                selectedEncounter
                  ? handleUpdateEncounter
                  : handleCreateEncounter
              }
              onCancel={() => {
                setShowEncounterForm(false);
                setSelectedEncounter(null);
              }}
              isLoading={isLoading}
            />
          </div>
        </div>
      )}
    </div>
  );
}
