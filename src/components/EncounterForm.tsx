import React, { useEffect, useState } from 'react';
import { EncounterType, SOAPNotesType } from '../types';

interface EncounterFormProps {
  encounter?: EncounterType | null;
  patientId?: string;
  onSubmit: (data: any) => void;
  onCancel: () => void;
  isLoading?: boolean;
}

export function EncounterForm({
  encounter,
  patientId,
  onSubmit,
  onCancel,
  isLoading = false,
}: EncounterFormProps) {
  const [formData, setFormData] = useState({
    provider_id: '',
    date_created: '',
    note_text: '',
    diagnostic_codes: [] as string[],
    status: '',
    soap_notes: {
      subjective: '',
      objective: '',
      assessment: '',
      plan: '',
    } as SOAPNotesType,
  });

  const [diagnosticCode, setDiagnosticCode] = useState('');

  useEffect(() => {
    if (encounter) {
      setFormData({
        provider_id: encounter.provider_id || '',
        date_created: encounter.date_created
          ? encounter.date_created.split('T')[0]
          : '',
        note_text:
          typeof encounter.note_text === 'string' ? encounter.note_text : '',
        diagnostic_codes: encounter.diagnostic_codes || [],
        status: encounter.status || '',
        soap_notes: {
          subjective: '',
          objective: '',
          assessment: '',
          plan: '',
        },
      });

      // Check if note_text is a SOAP object
      if (
        typeof encounter.note_text === 'object' &&
        encounter.note_text !== null
      ) {
        setFormData(prev => ({
          ...prev,
          soap_notes: encounter.note_text as SOAPNotesType,
        }));
      }
    } else {
      // Set default date for new encounters
      setFormData(prev => ({
        ...prev,
        date_created: new Date().toISOString().split('T')[0],
      }));
    }
  }, [encounter]);

  const handleInputChange = (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement
    >
  ) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSOAPChange = (field: keyof SOAPNotesType, value: string) => {
    setFormData(prev => ({
      ...prev,
      soap_notes: {
        ...prev.soap_notes,
        [field]: value,
      },
    }));
  };

  const addDiagnosticCode = () => {
    if (diagnosticCode.trim()) {
      setFormData(prev => ({
        ...prev,
        diagnostic_codes: [...prev.diagnostic_codes, diagnosticCode.trim()],
      }));
      setDiagnosticCode('');
    }
  };

  const removeDiagnosticCode = (index: number) => {
    setFormData(prev => ({
      ...prev,
      diagnostic_codes: prev.diagnostic_codes.filter((_, i) => i !== index),
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    const submitData: any = {
      ...formData,
      note_text: formData.soap_notes,
    };

    // Remove soap_notes from submit data since we're using it as note_text
    delete submitData.soap_notes;

    onSubmit(submitData);
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-white rounded-lg shadow">
      <h2 className="text-2xl font-bold mb-6 text-gray-900">
        {encounter ? 'Edit Encounter' : 'New Encounter'}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-8">
        {/* Basic Information */}
        <div className="bg-gray-50 p-6 rounded-lg">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">
            Basic Information
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Provider ID *
              </label>
              <input
                type="text"
                name="provider_id"
                value={formData.provider_id}
                onChange={handleInputChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="e.g., DR001"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Date *
              </label>
              <input
                type="date"
                name="date_created"
                value={formData.date_created}
                onChange={handleInputChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Status
              </label>
              <select
                name="status"
                value={formData.status}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="">Select Status</option>
                <option value="draft">Draft</option>
                <option value="completed">Completed</option>
                <option value="signed">Signed</option>
                <option value="locked">Locked</option>
              </select>
            </div>
          </div>
        </div>

        {/* SOAP Notes */}
        <div className="bg-white border border-gray-200 rounded-lg">
          <div className="bg-blue-50 px-6 py-4 border-b border-gray-200 rounded-t-lg">
            <h3 className="text-lg font-semibold text-blue-900">SOAP Notes</h3>
            <p className="text-sm text-blue-700 mt-1">
              Structured documentation of the patient encounter
            </p>
          </div>

          <div className="p-6 space-y-6">
            {/* Subjective */}
            <div className="border-l-4 border-blue-500 pl-4">
              <label className="block text-sm font-semibold text-blue-700 mb-2 uppercase tracking-wide">
                Subjective
              </label>
              <p className="text-xs text-gray-600 mb-2">
                Patient's symptoms, concerns, and history
              </p>
              <textarea
                value={formData.soap_notes.subjective}
                onChange={e => handleSOAPChange('subjective', e.target.value)}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Patient reports... (symptoms, concerns, history of present illness, review of systems, etc.)"
              />
            </div>

            {/* Objective */}
            <div className="border-l-4 border-green-500 pl-4">
              <label className="block text-sm font-semibold text-green-700 mb-2 uppercase tracking-wide">
                Objective
              </label>
              <p className="text-xs text-gray-600 mb-2">
                Physical examination findings, vital signs, lab results
              </p>
              <textarea
                value={formData.soap_notes.objective}
                onChange={e => handleSOAPChange('objective', e.target.value)}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500"
                placeholder="Physical examination reveals... (vital signs, physical findings, lab results, imaging, etc.)"
              />
            </div>

            {/* Assessment */}
            <div className="border-l-4 border-yellow-500 pl-4">
              <label className="block text-sm font-semibold text-yellow-700 mb-2 uppercase tracking-wide">
                Assessment
              </label>
              <p className="text-xs text-gray-600 mb-2">
                Diagnosis, differential diagnosis, clinical impressions
              </p>
              <textarea
                value={formData.soap_notes.assessment}
                onChange={e => handleSOAPChange('assessment', e.target.value)}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500"
                placeholder="Assessment includes... (primary diagnosis, differential diagnoses, clinical impressions, etc.)"
              />
            </div>

            {/* Plan */}
            <div className="border-l-4 border-red-500 pl-4">
              <label className="block text-sm font-semibold text-red-700 mb-2 uppercase tracking-wide">
                Plan
              </label>
              <p className="text-xs text-gray-600 mb-2">
                Treatment plan, medications, follow-up, patient instructions
              </p>
              <textarea
                value={formData.soap_notes.plan}
                onChange={e => handleSOAPChange('plan', e.target.value)}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-red-500"
                placeholder="Plan includes... (treatment, medications, follow-up appointments, patient education, etc.)"
              />
            </div>
          </div>
        </div>

        {/* Diagnostic Codes */}
        <div className="bg-gray-50 p-6 rounded-lg">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">
            Diagnostic Codes
          </h3>
          <div className="flex gap-2 mb-3">
            <input
              type="text"
              value={diagnosticCode}
              onChange={e => setDiagnosticCode(e.target.value)}
              placeholder="Enter ICD-10 or other diagnostic code"
              className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              onKeyPress={e =>
                e.key === 'Enter' && (e.preventDefault(), addDiagnosticCode())
              }
            />
            <button
              type="button"
              onClick={addDiagnosticCode}
              className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500"
            >
              Add
            </button>
          </div>
          {formData.diagnostic_codes.length > 0 && (
            <div className="flex flex-wrap gap-2">
              {formData.diagnostic_codes.map((code, index) => (
                <span
                  key={index}
                  className="inline-flex items-center px-3 py-1 rounded-full text-sm bg-blue-100 text-blue-800 border border-blue-200"
                >
                  {code}
                  <button
                    type="button"
                    onClick={() => removeDiagnosticCode(index)}
                    className="ml-2 text-blue-600 hover:text-blue-800 focus:outline-none"
                  >
                    ×
                  </button>
                </span>
              ))}
            </div>
          )}
        </div>

        {/* Action Buttons */}
        <div className="flex justify-end space-x-4 pt-4 border-t border-gray-200">
          <button
            type="button"
            onClick={onCancel}
            className="px-6 py-2 text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-500"
          >
            Cancel
          </button>
          <button
            type="submit"
            disabled={isLoading}
            className="px-6 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {isLoading
              ? 'Saving...'
              : encounter
                ? 'Update Encounter'
                : 'Create Encounter'}
          </button>
        </div>
      </form>
    </div>
  );
}
