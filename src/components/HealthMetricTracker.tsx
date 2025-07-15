import React, { useEffect, useState } from 'react';
import apiService from '../services/api';
import { Button, Card, Input, Label } from './FormComponents';
import { useUser } from './UserContext';
import AreaChart from './visualizations/AreaChart';
import BarChart from './visualizations/BarChart';
import LineChart from './visualizations/LineChart';
import ScatterChart from './visualizations/ScatterChart';

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

// New screen for visualizing metrics
export function HealthMetricVisualization() {
  const { user, isLoading: userLoading } = useUser();
  const [startDate, setStartDate] = useState<string>('');
  const [endDate, setEndDate] = useState<string>('');
  const [visualizationType, setVisualizationType] = useState<
    'line' | 'bar' | 'scatter' | 'area'
  >('line');
  const [metrics, setMetrics] = useState<MetricSet[]>([]);
  const [metricNames, setMetricNames] = useState<string[]>([]);
  const [selectedMetrics, setSelectedMetrics] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!user?.id) return;
    if (!startDate || !endDate) return;
    setLoading(true);
    setError(null);
    apiService
      .get(`/api/users/${user.id}/metrics`)
      .then(res => {
        // Filter by date range
        const filtered = (res.metrics || []).filter((set: MetricSet) => {
          return set.date >= startDate && set.date <= endDate;
        });
        setMetrics(filtered);
        // Collect all metric names
        const names = Array.from(
          new Set(
            filtered.flatMap((set: MetricSet) =>
              set.metrics.map(m => m.metric_name)
            )
          )
        ) as string[];
        setMetricNames(names);
        // If no metrics selected, select all by default
        if (names.length && selectedMetrics.length === 0)
          setSelectedMetrics(names);
      })
      .catch(() => setError('Failed to fetch metrics'))
      .finally(() => setLoading(false));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [user?.id, startDate, endDate]);

  // Handle checkbox toggle
  const handleMetricToggle = (metric: string) => {
    setSelectedMetrics(prev =>
      prev.includes(metric) ? prev.filter(m => m !== metric) : [...prev, metric]
    );
  };

  // Prepare data for the chart: { metricName: string, points: { date, value }[] }
  const chartData = React.useMemo(() => {
    return selectedMetrics.map(metricName => {
      const points: { date: string; value: number }[] = [];
      metrics.forEach(set => {
        set.metrics.forEach(m => {
          if (m.metric_name === metricName) {
            const value = parseFloat(m.metric_value);
            if (!isNaN(value)) {
              points.push({ date: set.date, value });
            }
          }
        });
      });
      return {
        metricName,
        points: points.sort((a, b) => a.date.localeCompare(b.date)),
      };
    });
  }, [metrics, selectedMetrics]);

  if (userLoading) return <div>Loading user...</div>;

  return (
    <Card className="p-6 space-y-4 w-full max-w-4xl mx-auto mt-8">
      <h2 className="text-xl font-semibold">Health Metrics Visualization</h2>
      {error && <div className="text-red-600">{error}</div>}
      <div className="flex flex-col md:flex-row gap-4 items-center">
        <div>
          <Label>Start Date</Label>
          <Input
            type="date"
            value={startDate}
            onChange={e => setStartDate(e.target.value)}
          />
        </div>
        <div>
          <Label>End Date</Label>
          <Input
            type="date"
            value={endDate}
            onChange={e => setEndDate(e.target.value)}
          />
        </div>
        <div>
          <Label>Visualization Type</Label>
          <select
            className="border rounded px-2 py-1"
            value={visualizationType}
            onChange={e =>
              setVisualizationType(
                e.target.value as 'line' | 'bar' | 'scatter' | 'area'
              )
            }
          >
            <option value="line">Line Chart</option>
            <option value="bar">Bar Chart (coming soon)</option>
            <option value="scatter">Scatter Plot (coming soon)</option>
            <option value="area">Area Chart</option>
          </select>
        </div>
        <div>
          <Label>Metrics to Display</Label>
          <div className="flex flex-col max-h-40 overflow-y-auto border rounded p-2 bg-gray-50">
            {metricNames.map(name => (
              <label key={name} className="flex items-center space-x-2">
                <input
                  type="checkbox"
                  checked={selectedMetrics.includes(name)}
                  onChange={() => handleMetricToggle(name)}
                />
                <span>{name}</span>
              </label>
            ))}
          </div>
        </div>
      </div>
      <div className="mt-8">
        {loading ? (
          <div>Loading chart...</div>
        ) : chartData.length === 0 || selectedMetrics.length === 0 ? (
          <div>No data for selected range/metric.</div>
        ) : visualizationType === 'line' ? (
          <LineChart data={chartData} />
        ) : visualizationType === 'bar' ? (
          <BarChart data={chartData} />
        ) : visualizationType === 'scatter' ? (
          <ScatterChart data={chartData} />
        ) : visualizationType === 'area' ? (
          <AreaChart data={chartData} />
        ) : (
          <div>Visualization type not implemented yet.</div>
        )}
      </div>
    </Card>
  );
}

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
