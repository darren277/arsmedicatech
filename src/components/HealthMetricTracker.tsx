import React, { useEffect, useState } from 'react';
import { metricsAPI } from '../services/api';
import { Button, Card, Input, Label } from './FormComponents';
import { useUser } from './UserContext';
import AreaChart from './visualizations/AreaChart';
import BarChart from './visualizations/BarChart';
import CalendarChart from './visualizations/CalendarChart';
import Heatmap from './visualizations/Heatmap';
import LineChart from './visualizations/LineChart';
import RadarChart from './visualizations/RadarChart';
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
function HealthMetricVisualization() {
  const { user, isLoading: userLoading } = useUser();
  const [startDate, setStartDate] = useState<string>('');
  const [endDate, setEndDate] = useState<string>('');
  const [visualizationType, setVisualizationType] = useState<
    'line' | 'bar' | 'scatter' | 'area' | 'radar' | 'heatmap' | 'calendar'
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
    metricsAPI
      .getAllForUser(user.id)
      .then(res => {
        // Filter by date range
        const filtered = (res.metrics || []).filter((set: MetricSet) => {
          return set.date >= startDate && set.date <= endDate;
        });
        setMetrics(filtered);
        // Collect all unique metric names across all sets
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
        if (filtered.length === 0) setError('No metrics found for this range.');
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
    // Build a map of date -> { metric_name: value }
    const allDates = metrics.map(set => set.date).sort();
    return selectedMetrics.map(metricName => {
      const points: { date: string; value: number | null }[] = allDates.map(
        date => {
          const set = metrics.find(s => s.date === date);
          const metric = set?.metrics.find(m => m.metric_name === metricName);
          // If value is missing or not a number, use null
          const value = metric ? parseFloat(metric.metric_value) : null;
          return { date, value: isNaN(value as number) ? null : value };
        }
      );
      return { metricName, points };
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
                e.target.value as
                  | 'line'
                  | 'bar'
                  | 'scatter'
                  | 'area'
                  | 'radar'
                  | 'heatmap'
                  | 'calendar'
              )
            }
          >
            <option value="line">Line Chart</option>
            <option value="bar">Bar Chart</option>
            <option value="scatter">Scatter Plot</option>
            <option value="area">Area Chart</option>
            <option value="radar">Radar Chart</option>
            <option value="heatmap">Heatmap</option>
            <option value="calendar">Calendar Chart</option>
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
        ) : visualizationType === 'radar' ? (
          <RadarChart data={chartData} date={endDate} />
        ) : visualizationType === 'heatmap' ? (
          <Heatmap data={chartData} />
        ) : visualizationType === 'calendar' ? (
          <CalendarChart data={chartData} />
        ) : (
          <div>Visualization type not implemented yet.</div>
        )}
      </div>
    </Card>
  );
}

function HealthMetricTracker() {
  const { user, isLoading: userLoading } = useUser();
  const [metrics, setMetrics] = useState<Metric[]>([
    { metric_name: '', metric_value: '', metric_unit: '' },
  ]);
  const [date, setDate] = useState<Date | undefined>(() => new Date());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [fetching, setFetching] = useState(false);

  // Fetch metrics for user and date on mount and when date changes
  useEffect(() => {
    if (!user?.id || !date) return;
    setFetching(true);
    setError(null);
    const isoDate = date.toISOString().slice(0, 10);
    metricsAPI
      .getForUserByDate(user.id, isoDate)
      .then(res => {
        if (res && res.metrics && res.metrics.length > 0) {
          setMetrics(res.metrics);
        } else {
          setMetrics([{ metric_name: '', metric_value: '', metric_unit: '' }]);
        }
      })
      .catch(() => {
        setMetrics([{ metric_name: '', metric_value: '', metric_unit: '' }]);
      })
      .finally(() => setFetching(false));
  }, [user?.id, date]);

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
    if (!user?.id || !date) {
      setError('User not logged in or date not selected');
      setLoading(false);
      return;
    }
    const isoDate = date.toISOString().slice(0, 10);
    try {
      await metricsAPI.upsertForUserByDate(user.id, isoDate, metrics);
      setSuccess('Metrics saved!');
      // Refresh metrics for this date
      const res = await metricsAPI.getForUserByDate(user.id, isoDate);
      if (res && res.metrics && res.metrics.length > 0) {
        setMetrics(res.metrics);
      }
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
                    className="bg-blue-600 hover:bg-blue-700 text-white"
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
        <Button
          className="bg-blue-600 hover:bg-blue-700 text-white"
          onClick={addRow}
          disabled={loading}
        >
          + Add Metric
        </Button>
        <Button
          className="bg-green-600 hover:bg-green-700 text-white"
          onClick={handleSubmit}
          disabled={loading}
        >
          {loading ? 'Submitting...' : 'Submit'}
        </Button>
      </div>

      <Button
        className="bg-blue-600 hover:bg-blue-700 text-white"
        onClick={() => (window.location.href = '/health-metrics-visualization')}
      >
        Health Metrics Visualization
      </Button>
    </Card>
  );
}

export { HealthMetricTracker, HealthMetricVisualization };
