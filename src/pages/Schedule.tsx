import { useState } from 'react';
import Calendar from 'react-calendar';
import { Value } from 'react-calendar/dist/esm/shared/types.js';
import AppointmentForm from '../components/AppointmentForm';
import SignupPopup from '../components/SignupPopup';
import { useSignupPopup } from '../hooks/useSignupPopup';
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

  const handleCalendarChange = (
    value: Value,
    event?: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) => {
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

    setCalendarValue(selectedDate);
    setSelectedDate(selectedDate);
    setIsModalOpen(true);
  };

  const handleAppointmentSubmit = (appointmentData: any) => {
    const newAppointment: Appointment = {
      id: Date.now().toString(),
      patientName: appointmentData.patientName,
      appointmentDate: appointmentData.appointmentDate,
      startTime: appointmentData.startTime,
      endTime: appointmentData.endTime,
      appointmentType: appointmentData.appointmentType,
      status: 'scheduled',
      notes: appointmentData.notes,
      location: appointmentData.location,
    };

    setAppointments(prev => [...prev, newAppointment]);
    setSelectedDate(null);
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
      const dayAppointments = appointments.filter(apt =>
        isSameDay(date, new Date(apt.appointmentDate))
      );

      if (dayAppointments.length > 0) {
        return 'has-appointments';
      }
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
                onClick={() => {
                  setSelectedDate(new Date());
                  setIsModalOpen(true);
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

      <AppointmentForm
        isOpen={isModalOpen}
        onClose={() => {
          setIsModalOpen(false);
          setSelectedDate(null);
        }}
        selectedDate={selectedDate || undefined}
        onSubmit={handleAppointmentSubmit}
      />
    </>
  );
};

export default Schedule;
