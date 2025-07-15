import * as d3 from 'd3';
import React, { useEffect, useState } from 'react';
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

// LineChart component using d3
function LineChart({
  data,
  metricName,
}: {
  data: { date: string; value: number }[];
  metricName: string;
}) {
  const ref = React.useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    // Clear previous chart
    ref.current.innerHTML = '';
    if (!data.length) return;

    const margin = { top: 20, right: 30, bottom: 30, left: 40 };
    const width = 500 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;

    const svg = d3
      .select(ref.current)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // Parse dates
    const parseDate = d3.timeParse('%Y-%m-%d');
    const chartData = data.map(d => ({
      ...d,
      date: parseDate(d.date) as Date,
    }));

    // X and Y scales
    const x = d3
      .scaleTime()
      .domain(d3.extent(chartData, d => d.date) as [Date, Date])
      .range([0, width]);
    const y = d3
      .scaleLinear()
      .domain([
        d3.min(chartData, d => d.value) ?? 0,
        d3.max(chartData, d => d.value) ?? 1,
      ])
      .nice()
      .range([height, 0]);

    // X axis
    svg
      .append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x).ticks(5));

    // Y axis
    svg.append('g').call(d3.axisLeft(y));

    // Line
    svg
      .append('path')
      .datum(chartData)
      .attr('fill', 'none')
      .attr('stroke', '#2563eb')
      .attr('stroke-width', 2)
      .attr(
        'd',
        d3
          .line<{ date: Date; value: number }>()
          .x(d => x(d.date))
          .y(d => y(d.value))
      );

    // Dots
    svg
      .selectAll('dot')
      .data(chartData)
      .enter()
      .append('circle')
      .attr('cx', d => x(d.date))
      .attr('cy', d => y(d.value))
      .attr('r', 3)
      .attr('fill', '#2563eb');
  }, [data, metricName]);

  return <div ref={ref}></div>;
}

// New screen for visualizing metrics
export function HealthMetricVisualization() {
  const { user, isLoading: userLoading } = useUser();
  const [startDate, setStartDate] = useState<string>('');
  const [endDate, setEndDate] = useState<string>('');
  const [visualizationType, setVisualizationType] = useState<'line'>('line');
  const [metrics, setMetrics] = useState<MetricSet[]>([]);
  const [metricNames, setMetricNames] = useState<string[]>([]);
  const [selectedMetric, setSelectedMetric] = useState<string>('');
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
        if (names.length && !selectedMetric)
          setSelectedMetric(names[0] as string);
      })
      .catch(() => setError('Failed to fetch metrics'))
      .finally(() => setLoading(false));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [user?.id, startDate, endDate]);

  // Prepare data for the chart
  const chartData = React.useMemo(() => {
    if (!selectedMetric) return [];
    // Flatten all metric sets for the selected metric
    const points: { date: string; value: number }[] = [];
    metrics.forEach(set => {
      set.metrics.forEach(m => {
        if (m.metric_name === selectedMetric) {
          // Try to parse value as number
          const value = parseFloat(m.metric_value);
          if (!isNaN(value)) {
            points.push({ date: set.date, value });
          }
        }
      });
    });
    // Sort by date
    return points.sort((a, b) => a.date.localeCompare(b.date));
  }, [metrics, selectedMetric]);

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
            onChange={e => setVisualizationType(e.target.value as 'line')}
          >
            <option value="line">Line Chart</option>
            {/* Add more options in the future */}
          </select>
        </div>
        <div>
          <Label>Metric</Label>
          <select
            className="border rounded px-2 py-1"
            value={selectedMetric}
            onChange={e => setSelectedMetric(e.target.value)}
            disabled={metricNames.length === 0}
          >
            {metricNames.map(name => (
              <option key={name} value={name}>
                {name}
              </option>
            ))}
          </select>
        </div>
      </div>
      <div className="mt-8">
        {loading ? (
          <div>Loading chart...</div>
        ) : chartData.length === 0 ? (
          <div>No data for selected range/metric.</div>
        ) : (
          <LineChart data={chartData} metricName={selectedMetric} />
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
