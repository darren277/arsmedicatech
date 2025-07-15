import { useEffect, useState } from 'react';
import apiService from '../services/api';
import { Button, Card, Input, Label } from './FormComponents';
import { useUser } from './UserContext';

type Metric = {
  metric_name: string;
  metric_value: string;
  metric_unit: string;
};

type MetricSet = {
  user_id: string;
  date: string;
  metrics: Metric[];
};

export default function HealthMetricTracker() {
  const { user, isLoading: userLoading } = useUser();
  const [metrics, setMetrics] = useState<Metric[]>([
    { metric_name: '', metric_value: '', metric_unit: '' },
  ]);
  const [date, setDate] = useState<Date | undefined>(new Date());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [previousMetrics, setPreviousMetrics] = useState<MetricSet[]>([]);
  const [fetching, setFetching] = useState(false);

  useEffect(() => {
    if (!user?.id) return;
    setFetching(true);
    apiService
      .get(`/api/users/${user.id}/metrics`)
      .then(res => {
        setPreviousMetrics(res.metrics || []);
        setError(null);
      })
      .catch(err => {
        setError('Failed to fetch previous metrics');
      })
      .finally(() => setFetching(false));
  }, [user?.id]);

  const handleMetricChange = (
    index: number,
    field: keyof Metric,
    value: string
  ) => {
    const updated = [...metrics];
    updated[index][field] = value;
    setMetrics(updated);
  };

  const addRow = () => {
    setMetrics([
      ...metrics,
      { metric_name: '', metric_value: '', metric_unit: '' },
    ]);
  };

  const removeRow = (index: number) => {
    if (metrics.length > 1) {
      const updated = [...metrics];
      updated.splice(index, 1);
      setMetrics(updated);
    }
  };

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    setSuccess(null);
    if (!user?.id) {
      setError('User not logged in');
      setLoading(false);
      return;
    }
    const payload = {
      date: date ? date.toISOString().slice(0, 10) : '',
      metrics,
    };
    try {
      await apiService.post(`/api/users/${user.id}/metrics`, payload);
      setSuccess('Metrics saved!');
      // Refresh previous metrics
      const res = await apiService.get(`/api/users/${user.id}/metrics`);
      setPreviousMetrics(res.metrics || []);
    } catch (err) {
      setError('Failed to save metrics');
    } finally {
      setLoading(false);
    }
  };

  if (userLoading) return <div>Loading user...</div>;

  return (
    <Card className="p-6 space-y-4 w-full max-w-4xl mx-auto mt-8">
      <h2 className="text-xl font-semibold">Health Metric KPI Tracker</h2>

      {error && <div className="text-red-600">{error}</div>}
      {success && <div className="text-green-600">{success}</div>}

      <div>
        <Label className="mb-2 block">Select Date</Label>
        <Input
          type="date"
          placeholder="Date"
          value={date ? date.toISOString().slice(0, 10) : ''}
          onChange={e =>
            setDate(e.target.value ? new Date(e.target.value) : undefined)
          }
        />
      </div>

      <div className="overflow-x-auto">
        <table className="w-full border border-gray-300 rounded-md text-sm">
          <thead>
            <tr className="bg-gray-100 text-left">
              <th className="p-2 border">Metric Name</th>
              <th className="p-2 border">Value</th>
              <th className="p-2 border">Unit</th>
              <th className="p-2 border">Actions</th>
            </tr>
          </thead>
          <tbody>
            {metrics.map((metric, index) => (
              <tr key={index}>
                <td className="p-2 border">
                  <Input
                    value={metric.metric_name}
                    onChange={e =>
                      handleMetricChange(index, 'metric_name', e.target.value)
                    }
                    placeholder="e.g., Blood Pressure"
                  />
                </td>
                <td className="p-2 border">
                  <Input
                    value={metric.metric_value}
                    onChange={e =>
                      handleMetricChange(index, 'metric_value', e.target.value)
                    }
                    placeholder="e.g., 120/80"
                  />
                </td>
                <td className="p-2 border">
                  <Input
                    value={metric.metric_unit}
                    onChange={e =>
                      handleMetricChange(index, 'metric_unit', e.target.value)
                    }
                    placeholder="e.g., mmHg"
                  />
                </td>
                <td className="p-2 border">
                  <Button
                    variant="secondary"
                    onClick={() => removeRow(index)}
                    disabled={metrics.length === 1}
                  >
                    Remove
                  </Button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="flex justify-between items-center pt-4">
        <Button variant="secondary" onClick={addRow} disabled={loading}>
          + Add Metric
        </Button>
        <Button onClick={handleSubmit} disabled={loading}>
          {loading ? 'Submitting...' : 'Submit'}
        </Button>
      </div>

      {/* Previous Metrics Table */}
      <div className="mt-8">
        <h3 className="text-lg font-semibold mb-2">Previous Metrics</h3>
        {fetching ? (
          <div>Loading previous metrics...</div>
        ) : previousMetrics.length === 0 ? (
          <div>No previous metrics found.</div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full border border-gray-300 rounded-md text-sm">
              <thead>
                <tr className="bg-gray-50 text-left">
                  <th className="p-2 border">Date</th>
                  <th className="p-2 border">Metric Name</th>
                  <th className="p-2 border">Value</th>
                  <th className="p-2 border">Unit</th>
                </tr>
              </thead>
              <tbody>
                {previousMetrics.map((set, i) =>
                  set.metrics.map((metric, j) => (
                    <tr key={`${i}-${j}`}>
                      <td className="p-2 border">{set.date}</td>
                      <td className="p-2 border">{metric.metric_name}</td>
                      <td className="p-2 border">{metric.metric_value}</td>
                      <td className="p-2 border">{metric.metric_unit}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </Card>
  );
}
