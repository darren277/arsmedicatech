import React, { useEffect, useState } from 'react';

interface OrganizationFormProps {
  onSuccess?: (org: any) => void;
  createdBy: string;
  initialValues?: {
    name?: string;
    org_type?: string;
    description?: string;
    [key: string]: any;
  };
}

const ORG_TYPES = [
  { value: 'individual', label: 'Individual' },
  { value: 'provider', label: 'Provider' },
  { value: 'admin', label: 'Administrator' },
];

const OrganizationForm: React.FC<OrganizationFormProps> = ({
  onSuccess,
  createdBy,
  initialValues,
}) => {
  const [name, setName] = useState(initialValues?.name || '');
  const [orgType, setOrgType] = useState(
    initialValues?.org_type || ORG_TYPES[0].value
  );
  const [description, setDescription] = useState(
    initialValues?.description || ''
  );
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  useEffect(() => {
    if (initialValues) {
      setName(initialValues.name || '');
      setOrgType(initialValues.org_type || ORG_TYPES[0].value);
      setDescription(initialValues.description || '');
    }
  }, [initialValues]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);
    setLoading(true);
    try {
      // If editing, don't POST, just call onSuccess with updated data
      if (initialValues) {
        const updated = {
          ...initialValues,
          name,
          org_type: orgType,
          description,
          created_by: createdBy,
        };
        if (onSuccess) onSuccess(updated);
        setSuccess('Organization updated successfully!');
        setLoading(false);
        return;
      }
      const res = await fetch('/api/organizations', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name,
          org_type: orgType,
          description,
          created_by: createdBy,
        }),
      });
      const data = await res.json();
      if (res.ok) {
        setSuccess('Organization created successfully!');
        setName('');
        setOrgType(ORG_TYPES[0].value);
        setDescription('');
        if (onSuccess) onSuccess(data.organization);
      } else {
        setError(data.error || 'Failed to create organization');
      }
    } catch (err: any) {
      setError(err.message || 'Network error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="organization-form">
      <h2>{initialValues ? 'Edit Organization' : 'Create Organization'}</h2>
      <div>
        <label>Organization Name</label>
        <input
          type="text"
          value={name}
          onChange={e => setName(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Type</label>
        <select value={orgType} onChange={e => setOrgType(e.target.value)}>
          {ORG_TYPES.map(opt => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
      </div>
      <div>
        <label>Description</label>
        <textarea
          value={description}
          onChange={e => setDescription(e.target.value)}
        />
      </div>
      <button type="submit" disabled={loading}>
        {loading
          ? initialValues
            ? 'Saving...'
            : 'Creating...'
          : initialValues
            ? 'Save Changes'
            : 'Create Organization'}
      </button>
      {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
      {success && <div style={{ color: 'green', marginTop: 8 }}>{success}</div>}
    </form>
  );
};

export default OrganizationForm;
