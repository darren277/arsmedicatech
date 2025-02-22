import React from 'react';
import {useState} from 'react';
import Calendar from 'react-calendar';


function isSameDay (date1, date2) {
    return date1.getDate() === date2.getDate() && date1.getMonth() === date2.getMonth() && date1.getFullYear() === date2.getFullYear();
}

//const datesToAddContentTo = [tomorrow, in3Days, in5Days];
const datesToAddContentTo = [new Date(2025, 1, 1), new Date(2022, 2, 1), new Date(2022, 3, 1)];

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
    function onCalendarChange(nextValue) {setCalendarValue(nextValue);}

    return (
        <div>
            <h2>Schedule Page</h2>
            <Calendar onChange={onCalendarChange} value={calendarValue} tileContent={tileContent} tileClassName={tileClassName} />
        </div>
    )
};

export default Schedule;
