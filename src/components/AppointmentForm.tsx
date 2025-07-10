import React, { useState } from 'react';

interface AppointmentFormProps {
  isOpen: boolean;
  onClose: () => void;
  selectedDate?: Date;
  onSubmit?: (appointmentData: any) => void;
}

const AppointmentForm: React.FC<AppointmentFormProps> = ({
  isOpen,
  onClose,
  selectedDate,
  onSubmit,
}) => {
  const [formData, setFormData] = useState({
    patientName: '',
    appointmentDate: selectedDate
      ? selectedDate.toISOString().split('T')[0]
      : '',
    startTime: '09:00',
    endTime: '09:30',
    appointmentType: 'consultation',
    notes: '',
    location: '',
  });

  // Update form data when selectedDate changes
  React.useEffect(() => {
    if (selectedDate) {
      setFormData(prev => ({
        ...prev,
        appointmentDate: selectedDate.toISOString().split('T')[0],
      }));
    }
  }, [selectedDate]);

  console.log('AppointmentForm - selectedDate:', selectedDate);
  console.log(
    'AppointmentForm - formData.appointmentDate:',
    formData.appointmentDate
  );

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit?.(formData);
    onClose();
  };

  const handleInputChange = (field: string, value: string) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center"
      style={{
        zIndex: 9999,
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
      }}
      onClick={e => {
        if (e.target === e.currentTarget) {
          onClose();
        }
      }}
    >
      <div
        className="bg-white rounded-lg p-6 w-full max-w-md mx-4 shadow-xl border border-gray-200"
        style={{
          backgroundColor: 'white',
          zIndex: 10000,
          border: '3px solid red',
          minHeight: '400px',
        }}
      >
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-gray-800">New Appointment</h2>
          <button
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700 text-3xl font-bold w-8 h-8 flex items-center justify-center rounded-full hover:bg-gray-100"
          >
            x
          </button>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Patient Name *
            </label>
            <input
              type="text"
              value={formData.patientName}
              onChange={e => handleInputChange('patientName', e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Date *
            </label>
            {selectedDate && (
              <div className="mb-2 p-2 bg-blue-50 border border-blue-200 rounded-md">
                <span className="text-sm text-blue-700">
                  Selected: {selectedDate.toLocaleDateString()}
                </span>
              </div>
            )}
            <input
              type="date"
              value={formData.appointmentDate}
              onChange={e =>
                handleInputChange('appointmentDate', e.target.value)
              }
              className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Start Time *
              </label>
              <input
                type="time"
                value={formData.startTime}
                onChange={e => handleInputChange('startTime', e.target.value)}
                className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                End Time *
              </label>
              <input
                type="time"
                value={formData.endTime}
                onChange={e => handleInputChange('endTime', e.target.value)}
                className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Type
            </label>
            <select
              value={formData.appointmentType}
              onChange={e =>
                handleInputChange('appointmentType', e.target.value)
              }
              className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            >
              <option value="consultation">Consultation</option>
              <option value="follow_up">Follow-up</option>
              <option value="emergency">Emergency</option>
              <option value="routine">Routine Check-up</option>
              <option value="specialist">Specialist Visit</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Location
            </label>
            <input
              type="text"
              value={formData.location}
              onChange={e => handleInputChange('location', e.target.value)}
              placeholder="Room number, building, etc."
              className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Notes
            </label>
            <textarea
              value={formData.notes}
              onChange={e => handleInputChange('notes', e.target.value)}
              placeholder="Additional notes about the appointment"
              rows={3}
              className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>

          <div className="flex justify-end space-x-3 pt-6 border-t border-gray-200">
            <button
              type="button"
              onClick={onClose}
              className="px-6 py-2 text-gray-600 border border-gray-300 rounded-md hover:bg-gray-50 font-medium"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 font-medium shadow-sm"
            >
              Create Appointment
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AppointmentForm;
