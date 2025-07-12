import React, { useState } from 'react';
import { API_URL } from '../env_vars';

const NotificationTest: React.FC = () => {
  const [status, setStatus] = useState<string>('');

  const testSSE = async () => {
    try {
      setStatus('Testing SSE...');
      const response = await fetch(`${API_URL}/api/sse`, {
        method: 'GET',
        credentials: 'include',
      });

      if (response.ok) {
        setStatus('SSE test event sent! Check console for notifications.');
      } else {
        setStatus('SSE test failed. Make sure you are logged in.');
      }
    } catch (error) {
      setStatus(`SSE test error: ${error}`);
    }
  };

  const testAppointmentReminder = async () => {
    try {
      setStatus('Sending appointment reminder...');
      // This would be a real endpoint in production
      const response = await fetch(`${API_URL}/api/test/appointment-reminder`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          appointmentId: 'test-123',
          time: new Date().toISOString(),
          content: 'Test appointment reminder',
        }),
      });

      if (response.ok) {
        setStatus('Appointment reminder sent!');
      } else {
        setStatus('Appointment reminder test failed.');
      }
    } catch (error) {
      setStatus(`Appointment reminder error: ${error}`);
    }
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', margin: '10px' }}>
      <h3>SSE Notification Test</h3>
      <p>Use these buttons to test the Server-Sent Events functionality:</p>

      <div style={{ marginBottom: '10px' }}>
        <button
          onClick={testSSE}
          style={{
            padding: '8px 16px',
            marginRight: '10px',
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
          }}
        >
          Test SSE Message
        </button>

        <button
          onClick={testAppointmentReminder}
          style={{
            padding: '8px 16px',
            backgroundColor: '#28a745',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
          }}
        >
          Test Appointment Reminder
        </button>
      </div>

      {status && (
        <div
          style={{
            padding: '10px',
            backgroundColor: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '4px',
          }}
        >
          <strong>Status:</strong> {status}
        </div>
      )}

      <div style={{ marginTop: '15px', fontSize: '14px', color: '#666' }}>
        <p>
          <strong>Instructions:</strong>
        </p>
        <ul>
          <li>Make sure you are logged in</li>
          <li>Open the browser console to see event logs</li>
          <li>Check the Messages page to see real-time updates</li>
        </ul>
      </div>
    </div>
  );
};

export default NotificationTest;
