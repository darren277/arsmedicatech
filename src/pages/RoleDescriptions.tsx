import React from 'react';

const ROLE_LABELS: Record<string, string> = {
  patient: 'Individual',
  provider: 'Healthcare provider',
  administrator: 'Administrator for a clinic',
};

const ROLE_DESCRIPTIONS: Record<string, string> = {
  patient: 'Looking to manage or better understand their own health.',
  provider: 'Not affiliated with an existing clinic in our system.',
  administrator: 'You want to manage a clinic.',
};

const RoleDescriptions: React.FC = () => (
  <div style={{ maxWidth: 600, margin: '40px auto', padding: 24 }}>
    <h1 style={{ fontSize: 32, fontWeight: 700, marginBottom: 16 }}>
      User Roles
    </h1>
    <p style={{ color: '#555', marginBottom: 32 }}>
      When creating an account, you can choose the role that best fits your
      needs. Here’s what each role means:
    </p>
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
      {Object.entries(ROLE_LABELS).map(([role, label]) => (
        <div
          key={role}
          style={{
            border: '1px solid #e1e5e9',
            borderRadius: 10,
            padding: 24,
            background: '#fafbfc',
            boxShadow: '0 2px 8px rgba(0,0,0,0.03)',
          }}
        >
          <div style={{ fontSize: 22, fontWeight: 600, marginBottom: 8 }}>
            {label}
          </div>
          <div style={{ color: '#666', fontSize: 16 }}>
            {ROLE_DESCRIPTIONS[role]}
          </div>
        </div>
      ))}
    </div>
    <p style={{ color: '#555', marginTop: 32 }}>
      If you are affiliated with a clinic that you know to be in our system, you
      will need to reach out to your clinic administrator to get access.
    </p>
  </div>
);

export default RoleDescriptions;
