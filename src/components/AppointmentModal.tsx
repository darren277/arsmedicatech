import React, { useEffect, useState } from 'react';
import { patientAPI } from '../services/api';
import {
  Appointment,
  CreateAppointmentData,
  appointmentService,
} from '../services/appointments';

interface AppointmentModalProps {
  isOpen: boolean;
  onClose: () => void;
  selectedDate?: Date;
  selectedTime?: string;
  appointment?: Appointment;
  onAppointmentCreated?: (appointment: Appointment) => void;
  onAppointmentUpdated?: (appointment: Appointment) => void;
}

interface Patient {
  id: string;
  first_name: string;
  last_name: string;
  demographic_no: string;
}

const AppointmentModal: React.FC<AppointmentModalProps> = ({
  isOpen,
  onClose,
  selectedDate,
  selectedTime,
  appointment,
  onAppointmentCreated,
  onAppointmentUpdated,
}) => {
  const [formData, setFormData] = useState<CreateAppointmentData>({
    patient_id: '',
    appointment_date: selectedDate
      ? selectedDate.toISOString().split('T')[0]
      : '',
    start_time: selectedTime || '09:00',
    end_time: '09:30',
    appointment_type: 'consultation',
    notes: '',
    location: '',
  });

  const [patients, setPatients] = useState<Patient[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [availableSlots, setAvailableSlots] = useState<
    Array<{ start_time: string; end_time: string }>
  >([]);

  useEffect(() => {
    if (isOpen) {
      loadPatients();
      if (selectedDate) {
        loadAvailableSlots(selectedDate.toISOString().split('T')[0]);
      }
    }
  }, [isOpen, selectedDate]);

  useEffect(() => {
    if (appointment) {
      setFormData({
        patient_id: appointment.patient_id,
        appointment_date: appointment.appointment_date,
        start_time: appointment.start_time,
        end_time: appointment.end_time,
        appointment_type: appointment.appointment_type,
        notes: appointment.notes || '',
        location: appointment.location || '',
      });
    }
  }, [appointment]);

  const loadPatients = async () => {
    try {
      const response = await patientAPI.getAll();
      setPatients(response.patients || []);
    } catch (error) {
      console.error('Error loading patients:', error);
      setError('Failed to load patients');
    }
  };

  const loadAvailableSlots = async (date: string) => {
    try {
      const slots = await appointmentService.getAvailableSlots(date);
      setAvailableSlots(slots);
    } catch (error) {
      console.error('Error loading available slots:', error);
    }
  };

  const handleInputChange = (
    field: keyof CreateAppointmentData,
    value: string
  ) => {
    setFormData(prev => ({ ...prev, [field]: value }));

    // If date or start time changes, update available slots
    if (field === 'appointment_date' || field === 'start_time') {
      if (field === 'appointment_date') {
        loadAvailableSlots(value);
      }
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      if (appointment) {
        // Update existing appointment
        await appointmentService.updateAppointment(appointment.id, formData);
        onAppointmentUpdated?.(appointment);
      } else {
        // Create new appointment
        const newAppointment =
          await appointmentService.createAppointment(formData);
        onAppointmentCreated?.(newAppointment);
      }
      onClose();
    } catch (error: any) {
      setError(error.message || 'Failed to save appointment');
    } finally {
      setLoading(false);
    }
  };

  const calculateEndTime = (
    startTime: string,
    durationMinutes: number = 30
  ) => {
    const [hours, minutes] = startTime.split(':').map(Number);
    const startDate = new Date();
    startDate.setHours(hours, minutes, 0, 0);
    startDate.setMinutes(startDate.getMinutes() + durationMinutes);
    return startDate.toTimeString().slice(0, 5);
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 w-full max-w-md max-h-[90vh] overflow-y-auto">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-semibold">
            {appointment ? 'Edit Appointment' : 'New Appointment'}
          </h2>
          <button
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700 text-2xl"
          >
            ×
          </button>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          {/* Patient Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Patient *
            </label>
            <select
              value={formData.patient_id}
              onChange={e => handleInputChange('patient_id', e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            >
              <option value="">Select a patient</option>
              {patients.map(patient => (
                <option key={patient.id} value={patient.id}>
                  {patient.first_name} {patient.last_name} (ID:{' '}
                  {patient.demographic_no})
                </option>
              ))}
            </select>
          </div>

          {/* Date */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Date *
            </label>
            <input
              type="date"
              value={formData.appointment_date}
              onChange={e =>
                handleInputChange('appointment_date', e.target.value)
              }
              className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>

          {/* Time Selection */}
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Start Time *
              </label>
              <select
                value={formData.start_time}
                onChange={e => {
                  handleInputChange('start_time', e.target.value);
                  handleInputChange(
                    'end_time',
                    calculateEndTime(e.target.value)
                  );
                }}
                className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              >
                {availableSlots.map(slot => (
                  <option key={slot.start_time} value={slot.start_time}>
                    {slot.start_time}
                  </option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                End Time *
              </label>
              <input
                type="time"
                value={formData.end_time}
                onChange={e => handleInputChange('end_time', e.target.value)}
                className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>
          </div>

          {/* Appointment Type */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Type
            </label>
            <select
              value={formData.appointment_type}
              onChange={e =>
                handleInputChange('appointment_type', e.target.value)
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

          {/* Location */}
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

          {/* Notes */}
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

          {/* Action Buttons */}
          <div className="flex justify-end space-x-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-gray-600 border border-gray-300 rounded-md hover:bg-gray-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
            >
              {loading ? 'Saving...' : appointment ? 'Update' : 'Create'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AppointmentModal;
