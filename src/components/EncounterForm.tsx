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

  const [useSOAP, setUseSOAP] = useState(false);
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
        setUseSOAP(true);
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
      note_text: useSOAP ? formData.soap_notes : formData.note_text,
    };

    // Remove soap_notes from submit data if not using SOAP
    if (!useSOAP) {
      delete submitData.soap_notes;
    }

    onSubmit(submitData);
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow">
      <h2 className="text-2xl font-bold mb-6">
        {encounter ? 'Edit Encounter' : 'New Encounter'}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
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
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
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
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
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
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select Status</option>
              <option value="draft">Draft</option>
              <option value="completed">Completed</option>
              <option value="signed">Signed</option>
              <option value="locked">Locked</option>
            </select>
          </div>
        </div>

        <div>
          <div className="flex items-center mb-4">
            <input
              type="checkbox"
              id="useSOAP"
              checked={useSOAP}
              onChange={e => setUseSOAP(e.target.checked)}
              className="mr-2"
            />
            <label
              htmlFor="useSOAP"
              className="text-sm font-medium text-gray-700"
            >
              Use SOAP Notes Format
            </label>
          </div>

          {useSOAP ? (
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Subjective
                </label>
                <textarea
                  value={formData.soap_notes.subjective}
                  onChange={e => handleSOAPChange('subjective', e.target.value)}
                  rows={3}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="Patient's symptoms and concerns..."
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Objective
                </label>
                <textarea
                  value={formData.soap_notes.objective}
                  onChange={e => handleSOAPChange('objective', e.target.value)}
                  rows={3}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="Physical examination findings, lab results..."
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Assessment
                </label>
                <textarea
                  value={formData.soap_notes.assessment}
                  onChange={e => handleSOAPChange('assessment', e.target.value)}
                  rows={3}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="Diagnosis and clinical impressions..."
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Plan
                </label>
                <textarea
                  value={formData.soap_notes.plan}
                  onChange={e => handleSOAPChange('plan', e.target.value)}
                  rows={3}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="Treatment plan, medications, follow-up..."
                />
              </div>
            </div>
          ) : (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Notes
              </label>
              <textarea
                name="note_text"
                value={formData.note_text}
                onChange={handleInputChange}
                rows={6}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Enter encounter notes..."
              />
            </div>
          )}
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Diagnostic Codes
          </label>
          <div className="flex gap-2 mb-2">
            <input
              type="text"
              value={diagnosticCode}
              onChange={e => setDiagnosticCode(e.target.value)}
              placeholder="Enter diagnostic code"
              className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="button"
              onClick={addDiagnosticCode}
              className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600"
            >
              Add
            </button>
          </div>
          {formData.diagnostic_codes.length > 0 && (
            <div className="flex flex-wrap gap-2">
              {formData.diagnostic_codes.map((code, index) => (
                <span
                  key={index}
                  className="inline-flex items-center px-3 py-1 rounded-full text-sm bg-blue-100 text-blue-800"
                >
                  {code}
                  <button
                    type="button"
                    onClick={() => removeDiagnosticCode(index)}
                    className="ml-2 text-blue-600 hover:text-blue-800"
                  >
                    ×
                  </button>
                </span>
              ))}
            </div>
          )}
        </div>

        <div className="flex justify-end space-x-4">
          <button
            type="button"
            onClick={onCancel}
            className="px-4 py-2 text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300"
          >
            Cancel
          </button>
          <button
            type="submit"
            disabled={isLoading}
            className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 disabled:opacity-50"
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
