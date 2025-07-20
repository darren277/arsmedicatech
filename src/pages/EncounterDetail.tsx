import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { EntityDetailsModal } from '../components/EntityDetailsModal';
import { encounterAPI } from '../services/api';
import { EncounterType, PatientType, SOAPNotesType } from '../types';

export function EncounterDetail() {
  const { encounterId } = useParams<{ encounterId: string }>();
  const navigate = useNavigate();
  const [encounter, setEncounter] = useState<EncounterType | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [entities, setEntities] = useState<any[]>([]);
  const [isExtractingEntities, setIsExtractingEntities] = useState(false);
  const [selectedEntity, setSelectedEntity] = useState<any | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    if (encounterId) {
      loadEncounterData();
    }
  }, [encounterId]);

  // Set up global click handler for entity clicks
  useEffect(() => {
    // Add global click handler for entity clicks
    (window as any).handleEntityClick = (entityJson: string) => {
      try {
        const entity = JSON.parse(entityJson);
        handleEntityClick(entity);
      } catch (error) {
        console.error('Error parsing entity JSON:', error);
      }
    };

    // Cleanup on unmount
    return () => {
      delete (window as any).handleEntityClick;
    };
  }, []);

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

  const extractEntities = async () => {
    if (!encounter?.note_text) {
      alert('No notes available to extract entities from');
      return;
    }

    setIsExtractingEntities(true);
    try {
      const result = await encounterAPI.extractEntitiesFromNotes(
        encounter.note_text,
        encounter.note_type || 'text'
      );

      // Combine all entities from the result
      const allEntities = [
        ...(result.entities || []),
        ...(result.normalized_entities || []),
        ...(result.icd_codes || []),
      ];

      setEntities(allEntities);
      console.log('Extracted entities:', allEntities);
    } catch (error) {
      console.error('Error extracting entities:', error);
      alert('Failed to extract entities. Please try again.');
    } finally {
      setIsExtractingEntities(false);
    }
  };

  const handleEntityClick = (entity: any) => {
    setSelectedEntity(entity);
    setIsModalOpen(true);
  };

  const renderSOAPNotes = (soapNotes: SOAPNotesType) => {
    // Helper function to format text with preserved newlines
    const formatText = (text: string) => {
      if (!text) return 'No notes available';
      // Replace escaped newlines with actual newlines and preserve formatting
      return text.replace(/\\n/g, '\n');
    };

    // Helper function to highlight entities in text
    const highlightEntities = (text: string) => {
      if (!entities.length) {
        return formatText(text);
      }

      // Sort entities by start position to process them in order
      const sortedEntities = [...entities].sort(
        (a, b) => a.start_char - b.start_char
      );

      let result = formatText(text);
      let offset = 0;

      sortedEntities.forEach(entity => {
        const start = entity.start_char + offset;
        const end = entity.end_char + offset;

        if (start >= 0 && end <= result.length && start < end) {
          const before = result.substring(0, start);
          const entityText = result.substring(start, end);
          const after = result.substring(end);

          const spanWrapper = `<span class="bg-yellow-200 cursor-pointer hover:bg-yellow-300 border-b-2 border-yellow-400" onclick="window.handleEntityClick('${JSON.stringify(entity).replace(/'/g, "\\'")}')">${entityText}</span>`;

          result = `${before}${spanWrapper}${after}`;

          // Update offset for next entity - calculate actual length difference
          offset += spanWrapper.length - entityText.length;
        }
      });

      return result;
    };

    return (
      <div className="space-y-4">
        <div>
          <h4 className="font-semibold text-blue-600">Subjective</h4>
          <div
            className="text-gray-700 bg-gray-50 p-3 rounded whitespace-pre-wrap"
            dangerouslySetInnerHTML={{
              __html: highlightEntities(soapNotes.subjective || ''),
            }}
          />
        </div>
        <div>
          <h4 className="font-semibold text-green-600">Objective</h4>
          <div
            className="text-gray-700 bg-gray-50 p-3 rounded whitespace-pre-wrap"
            dangerouslySetInnerHTML={{
              __html: highlightEntities(soapNotes.objective || ''),
            }}
          />
        </div>
        <div>
          <h4 className="font-semibold text-yellow-600">Assessment</h4>
          <div
            className="text-gray-700 bg-gray-50 p-3 rounded whitespace-pre-wrap"
            dangerouslySetInnerHTML={{
              __html: highlightEntities(soapNotes.assessment || ''),
            }}
          />
        </div>
        <div>
          <h4 className="font-semibold text-red-600">Plan</h4>
          <div
            className="text-gray-700 bg-gray-50 p-3 rounded whitespace-pre-wrap"
            dangerouslySetInnerHTML={{
              __html: highlightEntities(soapNotes.plan || ''),
            }}
          />
        </div>
      </div>
    );
  };

  const renderNoteText = (noteText: any, noteType?: string) => {
    // Check if it's SOAP notes based on note_type field or object structure
    if (
      noteType === 'soap' ||
      (typeof noteText === 'object' &&
        noteText !== null &&
        'subjective' in noteText &&
        'objective' in noteText &&
        'assessment' in noteText &&
        'plan' in noteText)
    ) {
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
        {renderNoteText(encounter.note_text, encounter.note_type)}
      </div>

      {/* Action Buttons */}
      <div className="mt-8 flex justify-center space-x-4">
        <button
          onClick={extractEntities}
          disabled={isExtractingEntities}
          className={`px-6 py-2 rounded ${
            isExtractingEntities
              ? 'bg-gray-400 text-white cursor-not-allowed'
              : 'bg-purple-500 text-white hover:bg-purple-600'
          }`}
        >
          {isExtractingEntities ? 'Extracting...' : 'Extract Entities'}
        </button>
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

      {/* Entity Details Modal */}
      <EntityDetailsModal
        entity={selectedEntity}
        isOpen={isModalOpen}
        onClose={() => {
          setIsModalOpen(false);
          setSelectedEntity(null);
        }}
      />
    </div>
  );
}
