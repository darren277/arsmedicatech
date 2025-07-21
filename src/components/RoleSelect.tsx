import React from 'react';

interface RoleSelectProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
  disabled?: boolean;
  style?: React.CSSProperties;
}

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

const RoleSelect: React.FC<RoleSelectProps> = ({
  value,
  onChange,
  disabled = false,
  style,
}) => {
  return (
    <div className="form-group" style={{ marginBottom: 24, ...style }}>
      <label
        htmlFor="role"
        style={{ fontWeight: 500, marginBottom: 4, display: 'block' }}
      >
        You are a...
      </label>
      <select
        id="role"
        name="role"
        value={value}
        onChange={onChange}
        disabled={disabled}
        style={{
          width: '100%',
          padding: '8px',
          borderRadius: 4,
          border: '1px solid #ccc',
          fontSize: 16,
        }}
      >
        {Object.entries(ROLE_LABELS).map(([role, label]) => (
          <option key={role} value={role}>
            {label}
          </option>
        ))}
      </select>
      {/* Contextual description for the selected role */}
      <div
        className="role-description"
        style={{
          marginTop: 8,
          color: '#666',
          fontSize: 14,
          minHeight: 18,
          textAlign: 'left',
        }}
      >
        {ROLE_DESCRIPTIONS[value]}
      </div>
      <div style={{ marginTop: 8 }}>
        <a
          href="/about/roles"
          style={{
            fontSize: 14,
            color: '#007bff',
            textDecoration: 'underline',
            cursor: 'pointer',
          }}
          target="_blank"
          rel="noopener noreferrer"
        >
          If you are unsure, read more here.
        </a>
      </div>
    </div>
  );
};

export default RoleSelect;
