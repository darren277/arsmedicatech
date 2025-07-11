import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { EncounterForm } from '../components/EncounterForm';
import { EncounterTable } from '../components/EncounterTable';
import { PatientFormModal } from '../components/PatientFormModal';
import { PatientTable } from '../components/PatientTable';
import SearchBox from '../components/SearchBox';
import { usePatientSearch } from '../hooks/usePatientSearch';
import { encounterAPI, patientAPI } from '../services/api';
import { EncounterType, PatientType } from '../types';

export function Patients() {
  const navigate = useNavigate();
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

  // Search functionality
  const {
    query,
    setQuery,
    results: searchResults,
    loading: searchLoading,
  } = usePatientSearch();

  // Load patients on component mount
  useEffect(() => {
    loadPatients();
  }, []);

  // Load encounters when switching to encounters tab, when patient selection changes, or on initial load
  useEffect(() => {
    console.log('[DEBUG] Encounters useEffect triggered:', {
      activeTab,
      selectedPatient,
    });
    if (activeTab === 'encounters') {
      if (selectedPatient?.demographic_no) {
        console.log('[DEBUG] Loading encounters for selected patient');
        loadPatientEncounters(selectedPatient.demographic_no);
      } else {
        console.log('[DEBUG] Loading all encounters');
        loadAllEncounters();
      }
    }
  }, [activeTab, selectedPatient]);

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

  const loadAllEncounters = async () => {
    console.log('[DEBUG] Loading all encounters...');
    setIsLoading(true);
    try {
      const data = await encounterAPI.getAll();
      console.log('[DEBUG] Encounters loaded:', data);
      setEncounters(data);
    } catch (error) {
      console.error('Error loading all encounters:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const loadPatientEncounters = async (patientId: string) => {
    console.log('[DEBUG] Loading encounters for patient:', patientId);
    setIsLoading(true);
    try {
      const data = await encounterAPI.getByPatient(patientId);
      console.log('[DEBUG] Patient encounters loaded:', data);
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
      if (selectedPatient?.demographic_no) {
        loadPatientEncounters(selectedPatient.demographic_no);
      } else {
        loadAllEncounters();
      }
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
      } else {
        loadAllEncounters();
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
        } else {
          loadAllEncounters();
        }
      } catch (error) {
        console.error('Error deleting encounter:', error);
      }
    }
  };

  const handlePatientView = (patient: PatientType) => {
    navigate(`/patients/${patient.demographic_no}`);
  };

  const handlePatientEdit = (patient: PatientType) => {
    setSelectedPatient(patient);
    setShowPatientForm(true);
  };

  const handlePatientRowClick = (patient: PatientType) => {
    navigate(`/patients/${patient.demographic_no}`);
  };

  const handlePatientSelect = (patient: PatientType) => {
    setSelectedPatient(patient);
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

  const clearPatientSelection = () => {
    setSelectedPatient(null);
  };

  const handleNewEncounter = () => {
    if (selectedPatient?.demographic_no) {
      // Navigate to the dedicated encounter creation page for the selected patient
      navigate(`/patients/${selectedPatient.demographic_no}/encounters/new`);
    } else {
      // No patient selected - show a message and switch to patients tab
      alert('Please select a patient first to create an encounter.');
      setActiveTab('patients');
    }
  };

  // Determine which data to show based on search results
  const getDisplayData = () => {
    if (query.trim().length >= 2 && searchResults.length > 0) {
      // Show search results
      return searchResults;
    }

    // Show regular data based on active tab
    if (activeTab === 'patients') {
      return patients;
    } else {
      return encounters;
    }
  };

  const isShowingSearchResults =
    query.trim().length >= 2 && searchResults.length > 0;

  // Get the appropriate data for the current tab
  const getPatientsData = () => {
    if (isShowingSearchResults) {
      // Filter search results to only show patients
      return searchResults.filter(
        (item: any) => !('patient' in item && item.patient)
      );
    }
    return patients;
  };

  const getEncountersData = () => {
    if (isShowingSearchResults) {
      // Filter search results to only show encounters
      return searchResults.filter(
        (item: any) => 'patient' in item && item.patient
      );
    }
    return encounters;
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Patient Management
        </h1>

        {/* Search Box */}
        <div className="mb-6">
          <SearchBox
            value={query}
            onChange={setQuery}
            loading={searchLoading}
          />
        </div>

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
              className={`py-2 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'encounters'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              Encounters{' '}
              {selectedPatient &&
                `(${selectedPatient.first_name} ${selectedPatient.last_name})`}
            </button>
          </nav>
        </div>

        {/* Action Buttons */}
        <div className="flex justify-between items-center mb-6">
          {activeTab === 'patients' && !isShowingSearchResults && (
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

          {activeTab === 'encounters' && !isShowingSearchResults && (
            <div className="flex gap-2">
              <button
                onClick={handleNewEncounter}
                className={`px-4 py-2 rounded-md ${
                  selectedPatient
                    ? 'bg-green-500 text-white hover:bg-green-600'
                    : 'bg-yellow-500 text-white hover:bg-yellow-600'
                }`}
              >
                {selectedPatient
                  ? 'Add New Encounter'
                  : 'Select Patient to Create Encounter'}
              </button>
              {selectedPatient && (
                <button
                  onClick={clearPatientSelection}
                  className="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600"
                >
                  View All Encounters
                </button>
              )}
            </div>
          )}

          {isShowingSearchResults && (
            <div className="text-sm text-gray-600">
              Showing {searchResults.length} search result
              {searchResults.length !== 1 ? 's' : ''}
            </div>
          )}
        </div>
      </div>

      {/* Content */}
      {activeTab === 'patients' && (
        <div>
          <PatientTable
            patients={getPatientsData()}
            isLoading={isLoading || searchLoading}
            onView={handlePatientView}
            onEdit={handlePatientEdit}
            onDelete={handleDeletePatient}
            onRowClick={handlePatientRowClick}
            onSelect={handlePatientSelect}
          />
        </div>
      )}

      {activeTab === 'encounters' && (
        <div>
          {selectedPatient && !isShowingSearchResults ? (
            <div className="mb-4 p-4 bg-blue-50 rounded-lg">
              <h3 className="text-lg font-semibold text-blue-900">
                Encounters for {selectedPatient.first_name}{' '}
                {selectedPatient.last_name}
              </h3>
              <p className="text-blue-700">
                Patient ID: {selectedPatient.demographic_no}
              </p>
            </div>
          ) : !isShowingSearchResults ? (
            <div className="mb-4 p-4 bg-gray-50 rounded-lg">
              <h3 className="text-lg font-semibold text-gray-900">
                All Encounters
              </h3>
              <p className="text-gray-700">
                Select a patient from the Patients tab to filter encounters or
                create new encounters
              </p>
            </div>
          ) : null}

          <EncounterTable
            encounters={getEncountersData()}
            isLoading={isLoading || searchLoading}
            onView={handleEncounterView}
            onEdit={handleEncounterEdit}
            onDelete={handleDeleteEncounter}
            onRowClick={handleEncounterRowClick}
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
