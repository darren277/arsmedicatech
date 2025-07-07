import { useState } from 'react';
import Calendar from 'react-calendar';
import SignupPopup from '../components/SignupPopup';
import { useSignupPopup } from '../hooks/useSignupPopup';
import authService from '../services/auth';

function isSameDay(date1, date2) {
  return (
    date1.getDate() === date2.getDate() &&
    date1.getMonth() === date2.getMonth() &&
    date1.getFullYear() === date2.getFullYear()
  );
}

//const datesToAddContentTo = [tomorrow, in3Days, in5Days];
const datesToAddContentTo = [
  new Date(2025, 1, 1),
  new Date(2022, 2, 1),
  new Date(2022, 3, 1),
];

function tileContent({ date, view }) {
  // Add class to tiles in month view only
  if (view === 'month') {
    // Check if a date React-Calendar wants to check is on the list of dates to add class to
    if (datesToAddContentTo.find(dDate => isSameDay(dDate, date))) {
      return 'My content';
    }
  }
}

function tileClassName({ date, view }) {
  const datesToAddClassTo = datesToAddContentTo;
  // Add class to tiles in month view only
  if (view === 'month') {
    // Check if a date React-Calendar wants to check is on the list of dates to add class to
    if (datesToAddClassTo.find(dDate => isSameDay(dDate, date))) {
      return 'myClassName';
    }
  }
}

const Schedule = () => {
  const [calendarValue, setCalendarValue] = useState(new Date());
  const isAuthenticated = authService.isAuthenticated();
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

  function onCalendarChange(nextValue) {
    if (!isAuthenticated) {
      showSignupPopup();
      return;
    }
    setCalendarValue(nextValue);
  }

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
        </div>
        <Calendar
          onChange={onCalendarChange}
          value={calendarValue}
          tileContent={tileContent}
          tileClassName={tileClassName}
          className={!isAuthenticated ? 'calendar-disabled' : ''}
        />
      </div>
      <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />
    </>
  );
};

export default Schedule;
