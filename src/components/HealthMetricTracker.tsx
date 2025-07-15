import React, { useState } from 'react';
import { Button, Card, Input, Label } from './FormComponents';

type Metric = {
  metric_name: string;
  metric_value: string;
  metric_unit: string;
};

export default function HealthMetricTracker() {
  const [metrics, setMetrics] = useState<Metric[]>([
    { metric_name: '', metric_value: '', metric_unit: '' },
  ]);
  const [date, setDate] = useState<Date | undefined>(new Date());

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

  const handleSubmit = () => {
    console.log('Submitted:', { date, metrics });
    // TODO: Replace with persistence logic (e.g., API call)
  };

  return (
    <Card className="p-6 space-y-4 w-full max-w-4xl mx-auto mt-8">
      <h2 className="text-xl font-semibold">Health Metric KPI Tracker</h2>

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
        <Button variant="secondary" onClick={addRow}>
          + Add Metric
        </Button>
        <Button onClick={handleSubmit}>Submit</Button>
      </div>
    </Card>
  );
}
