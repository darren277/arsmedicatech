import { useState } from 'react';
import Calendar from 'react-calendar';
import AppointmentForm from '../components/AppointmentForm';
import SignupPopup from '../components/SignupPopup';
import { useSignupPopup } from '../hooks/useSignupPopup';
import authService from '../services/auth';

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

  const handleCalendarChange = (value: Date | Date[] | null) => {
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

      <style jsx>{`
        .schedule-container {
          padding: 20px;
          max-width: 1200px;
          margin: 0 auto;
        }

        .schedule-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 20px;
        }

        .guest-notice {
          text-align: center;
          padding: 20px;
          background-color: #f8f9fa;
          border-radius: 8px;
        }

        .guest-action-button {
          background-color: #007bff;
          color: white;
          border: none;
          padding: 10px 20px;
          border-radius: 4px;
          cursor: pointer;
          margin-top: 10px;
        }

        .schedule-actions {
          display: flex;
          gap: 10px;
        }

        .btn-primary {
          background-color: #007bff;
          color: white;
          border: none;
          padding: 10px 20px;
          border-radius: 4px;
          cursor: pointer;
        }

        .calendar-container {
          margin-bottom: 30px;
        }

        .calendar-disabled {
          opacity: 0.6;
          pointer-events: none;
        }

        .appointment-indicators {
          display: flex;
          flex-wrap: wrap;
          gap: 2px;
          justify-content: center;
          margin-top: 2px;
        }

        .appointment-dot {
          width: 6px;
          height: 6px;
          border-radius: 50%;
        }

        .appointment-scheduled {
          background-color: #ffc107;
        }
        .appointment-confirmed {
          background-color: #28a745;
        }
        .appointment-cancelled {
          background-color: #dc3545;
        }
        .appointment-completed {
          background-color: #007bff;
        }
        .appointment-no_show {
          background-color: #6c757d;
        }

        .appointment-more {
          font-size: 8px;
          color: #666;
          margin-left: 2px;
        }

        .has-appointments {
          background-color: #f8f9fa;
        }

        .appointments-list {
          margin-top: 20px;
        }

        .appointments-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
          gap: 15px;
          margin-top: 15px;
        }

        .appointment-card {
          background-color: white;
          border: 1px solid #ddd;
          border-radius: 8px;
          padding: 15px;
          transition: box-shadow 0.2s;
        }

        .appointment-card:hover {
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .appointment-time {
          font-weight: bold;
          color: #333;
          margin-bottom: 5px;
        }

        .appointment-patient {
          font-weight: 500;
          color: #333;
          margin-bottom: 5px;
        }

        .appointment-type {
          color: #666;
          text-transform: capitalize;
          margin-bottom: 5px;
        }

        .appointment-status {
          display: inline-block;
          padding: 2px 8px;
          border-radius: 12px;
          font-size: 12px;
          color: white;
          text-transform: capitalize;
          margin-bottom: 5px;
        }

        .appointment-notes {
          font-size: 14px;
          color: #666;
          margin-top: 5px;
          font-style: italic;
        }

        .no-appointments {
          text-align: center;
          color: #666;
          font-style: italic;
          grid-column: 1 / -1;
        }
      `}</style>
    </>
  );
};

export default Schedule;
