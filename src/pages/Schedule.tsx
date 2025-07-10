import React, { useEffect, useState } from 'react';
import Calendar from 'react-calendar';
import { Value } from 'react-calendar/dist/esm/shared/types.js';
import AppointmentForm from '../components/AppointmentForm';
import SignupPopup from '../components/SignupPopup';
import { useSignupPopup } from '../hooks/useSignupPopup';
import { appointmentService } from '../services/appointments';
import authService from '../services/auth';
import './Schedule.css';

interface Appointment {
  id: string;
  patientName: string;
  appointmentDate: string;
  startTime: string;
  endTime: string;
  appointmentType: string;
  status: string;
  notes?: string;
  location?: string;
}

function isSameDay(date1: Date, date2: Date): boolean {
  return (
    date1.getDate() === date2.getDate() &&
    date1.getMonth() === date2.getMonth() &&
    date1.getFullYear() === date2.getFullYear()
  );
}

const Schedule = () => {
  const [calendarValue, setCalendarValue] = useState(new Date());
  const [appointments, setAppointments] = useState<Appointment[]>([]);
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const isAuthenticated = authService.isAuthenticated();
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

  useEffect(() => {
    const loadAppointments = async () => {
      if (isAuthenticated) {
        try {
          console.log('Loading appointments from backend...');
          const response = await appointmentService.getAppointments();
          console.log('Backend appointments response:', response);

          // Convert backend appointments to frontend format
          const convertedAppointments = response.appointments.map(apt => ({
            id: apt.id,
            patientName: `Patient ${apt.patient_id}`, // We'll need to get actual patient names later
            appointmentDate: apt.appointment_date,
            startTime: apt.start_time,
            endTime: apt.end_time,
            appointmentType: apt.appointment_type,
            status: apt.status,
            notes: apt.notes,
            location: apt.location,
          }));
          console.log('Converted appointments:', convertedAppointments);
          setAppointments(convertedAppointments);
        } catch (error) {
          console.error('Error loading appointments:', error);
          // For now, keep using local appointments if backend fails
        }
      }
    };

    loadAppointments();
  }, [isAuthenticated]);

  // Also load appointments when component becomes visible (for navigation back)
  useEffect(() => {
    const handleVisibilityChange = () => {
      if (!document.hidden && isAuthenticated) {
        console.log('Page became visible, refreshing appointments...');
        const loadAppointments = async () => {
          try {
            const response = await appointmentService.getAppointments();
            const convertedAppointments = response.appointments.map(apt => ({
              id: apt.id,
              patientName: `Patient ${apt.patient_id}`,
              appointmentDate: apt.appointment_date,
              startTime: apt.start_time,
              endTime: apt.end_time,
              appointmentType: apt.appointment_type,
              status: apt.status,
              notes: apt.notes,
              location: apt.location,
            }));
            setAppointments(convertedAppointments);
          } catch (error) {
            console.error('Error refreshing appointments:', error);
          }
        };
        loadAppointments();
      }
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    return () =>
      document.removeEventListener('visibilitychange', handleVisibilityChange);
  }, [isAuthenticated]);

  const handleCalendarChange = (
    value: Value,
    event?: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) => {
    console.log('Calendar change - value:', value);

    if (!isAuthenticated) {
      showSignupPopup();
      return;
    }

    let selectedDate: Date;
    if (value instanceof Date) {
      selectedDate = value;
    } else if (Array.isArray(value) && value[0] instanceof Date) {
      selectedDate = value[0];
    } else {
      selectedDate = new Date();
    }

    console.log('Setting selected date:', selectedDate);
    setCalendarValue(selectedDate);
    setSelectedDate(selectedDate);
    setIsModalOpen(true);
  };

  const [showSuccessMessage, setShowSuccessMessage] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState('');

  const refreshAppointments = async () => {
    if (isAuthenticated) {
      try {
        console.log('Refreshing appointments...');
        const response = await appointmentService.getAppointments();
        const convertedAppointments = response.appointments.map(apt => ({
          id: apt.id,
          patientName: `Patient ${apt.patient_id}`,
          appointmentDate: apt.appointment_date,
          startTime: apt.start_time,
          endTime: apt.end_time,
          appointmentType: apt.appointment_type,
          status: apt.status,
          notes: apt.notes,
          location: apt.location,
        }));
        setAppointments(convertedAppointments);
        console.log('Appointments refreshed:', convertedAppointments);
      } catch (error) {
        console.error('Error refreshing appointments:', error);
      }
    }
  };

  const handleAppointmentSubmit = async (appointmentData: any) => {
    console.log('Appointment submitted:', appointmentData);
    setIsSubmitting(true);
    setError('');

    try {
      // Convert frontend form data to backend format
      const backendData = {
        patient_id: '1', // For now, use a default patient ID - we'll need to implement patient selection
        appointment_date: appointmentData.appointmentDate,
        start_time: appointmentData.startTime,
        end_time: appointmentData.endTime,
        appointment_type: appointmentData.appointmentType,
        notes: appointmentData.notes,
        location: appointmentData.location,
      };

      console.log('Sending to backend:', backendData);

      // Send to backend
      const newBackendAppointment =
        await appointmentService.createAppointment(backendData);
      console.log('Backend response:', newBackendAppointment);

      // Refresh the appointments list from the backend
      await refreshAppointments();

      setSelectedDate(null);
      setIsModalOpen(false);

      // Show success message
      setShowSuccessMessage(true);
      setTimeout(() => setShowSuccessMessage(false), 3000);
    } catch (error) {
      console.error('Error creating appointment:', error);
      setError('Failed to create appointment. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const tileContent = ({ date, view }: { date: Date; view: string }) => {
    if (view === 'month') {
      const dayAppointments = appointments.filter(apt =>
        isSameDay(date, new Date(apt.appointmentDate))
      );

      if (dayAppointments.length > 0) {
        return (
          <div className="appointment-indicators">
            {dayAppointments.slice(0, 3).map(apt => (
              <div
                key={apt.id}
                className={`appointment-dot appointment-${apt.status}`}
                title={`${apt.startTime} - ${apt.appointmentType}`}
              />
            ))}
            {dayAppointments.length > 3 && (
              <div className="appointment-more">
                +{dayAppointments.length - 3}
              </div>
            )}
          </div>
        );
      }
    }
    return null;
  };

  const tileClassName = ({ date, view }: { date: Date; view: string }) => {
    if (view === 'month') {
      const classes: string[] = [];

      // Check if this date has appointments
      const dayAppointments = appointments.filter(apt =>
        isSameDay(date, new Date(apt.appointmentDate))
      );
      if (dayAppointments.length > 0) {
        classes.push('has-appointments');
      }

      // Check if this is the selected date
      if (selectedDate && isSameDay(date, selectedDate)) {
        classes.push('selected-date');
      }

      return classes.length > 0 ? classes.join(' ') : null;
    }
    return null;
  };

  const getAppointmentsForDate = (date: Date) => {
    return appointments
      .filter(apt => isSameDay(date, new Date(apt.appointmentDate)))
      .sort((a, b) => a.startTime.localeCompare(b.startTime));
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'confirmed':
        return 'bg-green-500';
      case 'cancelled':
        return 'bg-red-500';
      case 'completed':
        return 'bg-blue-500';
      case 'no_show':
        return 'bg-gray-500';
      default:
        return 'bg-yellow-500';
    }
  };

  return (
    <>
      <div className="schedule-container">
        <div className="schedule-header">
          <h2>Schedule</h2>
          {!isAuthenticated && (
            <div className="guest-notice">
              <p>Sign up to create and manage appointments</p>
              <button onClick={showSignupPopup} className="guest-action-button">
                Get Started
              </button>
            </div>
          )}
          {isAuthenticated && (
            <div className="schedule-actions">
              <button
                onClick={refreshAppointments}
                className="btn-primary mr-2"
                title="Refresh appointments"
              >
                ↻ Refresh
              </button>
              <button
                onClick={() => {
                  console.log('New Appointment button clicked');
                  setSelectedDate(new Date());
                  setIsModalOpen(true);
                  console.log('Modal should be open:', true);
                }}
                className="btn-primary"
              >
                New Appointment
              </button>
            </div>
          )}
        </div>

        <div className="calendar-container">
          <Calendar
            onChange={handleCalendarChange}
            value={calendarValue}
            tileContent={tileContent}
            tileClassName={tileClassName}
            className={!isAuthenticated ? 'calendar-disabled' : ''}
          />
        </div>

        {/* Appointments for selected date */}
        {selectedDate && isAuthenticated && (
          <div className="appointments-list">
            <h3>Appointments for {selectedDate.toLocaleDateString()}</h3>
            <div className="appointments-grid">
              {getAppointmentsForDate(selectedDate).map(appointment => (
                <div key={appointment.id} className="appointment-card">
                  <div className="appointment-time">
                    {appointment.startTime} - {appointment.endTime}
                  </div>
                  <div className="appointment-patient">
                    {appointment.patientName}
                  </div>
                  <div className="appointment-type">
                    {appointment.appointmentType}
                  </div>
                  <div
                    className={`appointment-status ${getStatusColor(appointment.status)}`}
                  >
                    {appointment.status}
                  </div>
                  {appointment.notes && (
                    <div className="appointment-notes">{appointment.notes}</div>
                  )}
                </div>
              ))}
              {getAppointmentsForDate(selectedDate).length === 0 && (
                <p className="no-appointments">
                  No appointments scheduled for this date.
                </p>
              )}
            </div>
          </div>
        )}
      </div>

      <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />

      {/* Success Message */}
      {showSuccessMessage && (
        <div className="fixed top-4 right-4 bg-green-500 text-white px-6 py-3 rounded-md shadow-lg z-50">
          Appointment created successfully!
        </div>
      )}

      {/* Error Message */}
      {error && (
        <div className="fixed top-4 right-4 bg-red-500 text-white px-6 py-3 rounded-md shadow-lg z-50">
          {error}
        </div>
      )}

      {/* Loading Overlay */}
      {isSubmitting && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 shadow-xl">
            <div className="text-center">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mb-2"></div>
              <p>Creating appointment...</p>
            </div>
          </div>
        </div>
      )}

      <AppointmentForm
        isOpen={isModalOpen}
        onClose={() => {
          console.log('Modal closing');
          setIsModalOpen(false);
          setSelectedDate(null);
        }}
        selectedDate={selectedDate || undefined}
        onSubmit={handleAppointmentSubmit}
        isSubmitting={isSubmitting}
      />

      {/* Debug info */}
      {process.env.NODE_ENV === 'development' && (
        <div
          style={{
            position: 'fixed',
            bottom: 10,
            right: 10,
            background: 'white',
            padding: 10,
            border: '1px solid #ccc',
            fontSize: '12px',
          }}
        >
          Modal Open: {isModalOpen.toString()}
          <br />
          Selected Date: {selectedDate?.toDateString() || 'None'}
          <br />
          Appointments: {appointments.length}
        </div>
      )}
    </>
  );
};

export default Schedule;
