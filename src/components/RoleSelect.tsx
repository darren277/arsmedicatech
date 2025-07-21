import React from 'react';

interface RoleSelectProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
  disabled?: boolean;
  style?: React.CSSProperties;
}

const RoleSelect: React.FC<RoleSelectProps> = ({
  value,
  onChange,
  disabled = false,
  style,
}) => (
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
      <option value="patient">
        Individual (looking to manage or better understand their own health)
      </option>
      <option value="provider">
        Healthcare provider (not affiliated with an existing clinic in our
        system)
      </option>
      <option value="administrator">Administrator for a clinic</option>
    </select>
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

export default RoleSelect;
