import React from 'react';
import UserNotesScreen from '../components/UserNotes';

const UserNotesPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <div className="bg-white rounded-lg shadow-lg overflow-hidden">
          <UserNotesScreen />
        </div>
      </div>
    </div>
  );
};

export default UserNotesPage;
