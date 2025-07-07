import { useState } from 'react';
import Calendar from 'react-calendar';
import { Value } from 'react-calendar/dist/cjs/shared/types';
import SignupPopup from '../components/SignupPopup';
import { useSignupPopup } from '../hooks/useSignupPopup';
import authService from '../services/auth';

function isSameDay(date1: Date, date2: Date): boolean {
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

function tileContent({
  date,
  view,
}: {
  date: Date;
  view: string;
}): string | null {
  // Add class to tiles in month view only
  if (view === 'month') {
    // Check if a date React-Calendar wants to check is on the list of dates to add class to
    if (datesToAddContentTo.find(dDate => isSameDay(dDate, date))) {
      return 'My content';
    }
  }
  return null;
}

function tileClassName({
  date,
  view,
}: {
  date: Date;
  view: string;
}): string | null {
  const datesToAddClassTo = datesToAddContentTo;
  // Add class to tiles in month view only
  if (view === 'month') {
    // Check if a date React-Calendar wants to check is on the list of dates to add class to
    if (datesToAddClassTo.find(dDate => isSameDay(dDate, date))) {
      return 'myClassName';
    }
  }
  return null;
}

const Schedule = () => {
  const [calendarValue, setCalendarValue] = useState(new Date());
  const isAuthenticated = authService.isAuthenticated();
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

  function onCalendarChange(
    value: Value,
    event: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ): void {
    if (!isAuthenticated) {
      showSignupPopup();
      return;
    }
    // Handle single date or range, fallback to today if null
    if (value instanceof Date) {
      setCalendarValue(value);
    } else if (Array.isArray(value) && value[0] instanceof Date) {
      setCalendarValue(value[0]);
    } else {
      setCalendarValue(new Date());
    }
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
