import React, { useEffect, useState } from 'react';
import OrganizationForm from '../components/OrganizationForm';
import { useUser } from '../components/UserContext';

const OrganizationPage: React.FC = () => {
  const { user, isAuthenticated, isLoading } = useUser();
  const [org, setOrg] = useState<any | null>(null);
  const [orgLoading, setOrgLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [editing, setEditing] = useState(false);

  // Fetch organization for the current user (if any)
  useEffect(() => {
    const fetchOrg = async () => {
      if (!user || !isAuthenticated) return;
      setOrgLoading(true);
      setError(null);
      try {
        // TODO: Replace with a real API call to fetch org by user
        // For now, try to fetch all orgs and find one created by this user
        const res = await fetch('/api/organizations');
        if (res.ok) {
          const data = await res.json();
          // Assume data.organizations is an array
          const found = Array.isArray(data.organizations)
            ? data.organizations.find((o: any) => o.created_by === user.id)
            : null;
          setOrg(found || null);
        } else {
          setError('Failed to fetch organization');
        }
      } catch (err: any) {
        setError(err.message || 'Network error');
      } finally {
        setOrgLoading(false);
      }
    };
    fetchOrg();
  }, [user, isAuthenticated]);

  const handleEdit = () => setEditing(true);
  const handleCancelEdit = () => setEditing(false);

  const handleUpdateOrg = async (updatedOrg: any) => {
    if (!org || !org.id) return;
    setError(null);
    setOrgLoading(true);
    try {
      const res = await fetch(`/api/organizations/${org.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updatedOrg),
      });
      const data = await res.json();
      if (res.ok) {
        setOrg(data.organization || updatedOrg);
        setEditing(false);
      } else {
        setError(data.error || 'Failed to update organization');
      }
    } catch (err: any) {
      setError(err.message || 'Network error');
    } finally {
      setOrgLoading(false);
    }
  };

  if (isLoading || orgLoading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated || !user) {
    return <div>You must be logged in to manage organizations.</div>;
  }

  if (user.role !== 'admin') {
    return <div>You do not have permission to manage organizations.</div>;
  }

  if (org) {
    if (editing) {
      return (
        <div>
          <h2>Edit Organization</h2>
          <OrganizationForm
            onSuccess={handleUpdateOrg}
            createdBy={user.id}
            initialValues={org}
          />
          <button onClick={handleCancelEdit} style={{ marginTop: 8 }}>
            Cancel
          </button>
          {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
        </div>
      );
    }
    return (
      <div>
        <h2>Organization Details</h2>
        <div>
          <strong>Name:</strong> {org.name}
        </div>
        <div>
          <strong>Type:</strong> {org.org_type}
        </div>
        <div>
          <strong>Description:</strong> {org.description}
        </div>
        <button onClick={handleEdit} style={{ marginTop: 8 }}>
          Edit
        </button>
        {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
      </div>
    );
  }

  return (
    <div>
      <OrganizationForm onSuccess={setOrg} createdBy={user.id} />
      {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
    </div>
  );
};

export default OrganizationPage;
