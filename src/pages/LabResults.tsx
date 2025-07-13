import React, { useEffect, useState } from 'react';
import apiService from '../services/api';
import { LabResult, LabResultsData } from '../types';

interface LabResultsTableProps {
  title: string;
  data: { [key: string]: LabResult };
}

interface RangeVisualizerProps {
  result: number;
  range: [number, number];
  units: string | null;
}

interface ResultStatusIndicatorProps {
  result: number;
  range: [number, number];
}

interface HoverModalProps {
  isOpen: boolean;
  onClose: () => void;
  description: string;
  name: string;
  result: number;
  range: [number, number];
  units: string | null;
  notes?: string;
}

const RangeVisualizer: React.FC<RangeVisualizerProps> = ({
  result,
  range,
  units,
}) => {
  const [min, max] = range;
  const rangeWidth = max - min;
  const resultPosition = ((result - min) / rangeWidth) * 100;

  // Clamp position between 0 and 100
  const clampedPosition = Math.max(0, Math.min(100, resultPosition));

  const isOutOfRange = result < min || result > max;

  return (
    <div className="flex items-center space-x-2">
      <div className="flex-1 relative">
        <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
          {/* Range bar */}
          <div className="h-full bg-green-200 relative">
            {/* Result indicator */}
            <div
              className={`absolute top-0 h-full w-1 rounded-full transition-all duration-200 ${
                isOutOfRange ? 'bg-red-500' : 'bg-blue-500'
              }`}
              style={{ left: `${clampedPosition}%` }}
            />
          </div>
        </div>
        {/* Range labels */}
        <div className="flex justify-between text-xs text-gray-600 mt-1">
          <span>{min}</span>
          <span>{max}</span>
        </div>
      </div>
      <span className="text-sm text-gray-700 min-w-[60px] text-right">
        {result}
        {units && <span className="text-gray-500 ml-1">{units}</span>}
      </span>
    </div>
  );
};

const ResultStatusIndicator: React.FC<ResultStatusIndicatorProps> = ({
  result,
  range,
}) => {
  const [min, max] = range;
  const isOutOfRange = result < min || result > max;

  if (!isOutOfRange) {
    return (
      <div
        className="w-3 h-3 bg-green-500 rounded-full flex-shrink-0"
        title="Within normal range"
      />
    );
  }

  return (
    <div
      className="w-3 h-3 bg-red-500 rounded-full flex-shrink-0 animate-pulse"
      title="Outside normal range"
    />
  );
};

const HoverModal: React.FC<HoverModalProps> = ({
  isOpen,
  onClose,
  description,
  name,
  result,
  range,
  units,
  notes,
}) => {
  if (!isOpen) return null;

  const [min, max] = range;
  const isOutOfRange = result < min || result > max;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 max-w-md w-full mx-4 shadow-xl">
        <div className="flex justify-between items-start mb-4">
          <h3 className="text-lg font-semibold text-gray-900">{name}</h3>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 text-xl font-bold"
          >
            ×
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <p className="text-sm text-gray-600 mb-2">{description}</p>
          </div>

          <div className="bg-gray-50 p-3 rounded">
            <div className="flex justify-between items-center mb-2">
              <span className="font-medium">Result:</span>
              <span
                className={`font-semibold ${isOutOfRange ? 'text-red-600' : 'text-green-600'}`}
              >
                {result} {units}
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="font-medium">Normal Range:</span>
              <span className="text-gray-700">
                {min} - {max} {units}
              </span>
            </div>
          </div>

          {notes && (
            <div>
              <span className="font-medium text-gray-700">Notes:</span>
              <p className="text-sm text-gray-600 mt-1">{notes}</p>
            </div>
          )}

          {isOutOfRange && (
            <div className="bg-red-50 border border-red-200 p-3 rounded">
              <p className="text-red-700 text-sm font-medium">
                ⚠️ Result is outside the normal range
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

const LabResultsTable: React.FC<LabResultsTableProps> = ({ title, data }) => {
  const [hoveredItem, setHoveredItem] = useState<string | null>(null);

  const items = Object.entries(data);

  if (items.length === 0) {
    return null;
  }

  return (
    <div className="mb-8">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">{title}</h2>
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Test Name
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Result & Range
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Notes
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {items.map(([name, labResult]) => (
              <tr
                key={name}
                className="hover:bg-gray-50 cursor-pointer transition-colors duration-150"
                onMouseEnter={() => setHoveredItem(name)}
                onMouseLeave={() => setHoveredItem(null)}
              >
                <td className="px-6 py-4 whitespace-nowrap">
                  <ResultStatusIndicator
                    result={labResult.result}
                    range={labResult.reference_range}
                  />
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm font-medium text-gray-900">
                    {name}
                  </div>
                </td>
                <td className="px-6 py-4">
                  <RangeVisualizer
                    result={labResult.result}
                    range={labResult.reference_range}
                    units={labResult.units}
                  />
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-500">
                    {labResult.notes || '-'}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Hover Modal */}
      {hoveredItem && data[hoveredItem] && (
        <HoverModal
          isOpen={true}
          onClose={() => setHoveredItem(null)}
          description={data[hoveredItem].description}
          name={hoveredItem}
          result={data[hoveredItem].result}
          range={data[hoveredItem].reference_range}
          units={data[hoveredItem].units}
          notes={data[hoveredItem].notes}
        />
      )}
    </div>
  );
};

const LabResults: React.FC = () => {
  const [labResults, setLabResults] = useState<LabResultsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchLabResults = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await apiService.getLabResults();
        setLabResults(data);
      } catch (err) {
        console.error('Failed to fetch lab results:', err);
        setError('Failed to load lab results. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchLabResults();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
            <p className="mt-4 text-gray-600">Loading lab results...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <p className="text-red-700">{error}</p>
              <button
                onClick={() => window.location.reload()}
                className="mt-2 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
              >
                Retry
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (!labResults) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <p className="text-gray-600">No lab results available.</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Lab Results</h1>
          <p className="mt-2 text-gray-600">
            Comprehensive laboratory test results with visual indicators and
            detailed information.
          </p>
        </div>

        <div className="space-y-8">
          <LabResultsTable title="Hematology" data={labResults.hematology} />

          <LabResultsTable
            title="Differential Hematology"
            data={labResults.differential_hematology}
          />

          <LabResultsTable
            title="General Chemistry"
            data={labResults.general_chemistry}
          />

          <LabResultsTable
            title="Serum Proteins"
            data={labResults.serum_proteins}
          />
        </div>

        <div className="mt-8 bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-800 mb-4">Legend</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-green-500 rounded-full"></div>
              <span>Within normal range</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-red-500 rounded-full"></div>
              <span>Outside normal range</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-blue-500 rounded-full"></div>
              <span>Result indicator on range bar</span>
            </div>
          </div>
          <p className="mt-4 text-sm text-gray-600">
            Hover over any test name to see detailed information about the test
            and its clinical significance.
          </p>
        </div>
      </div>
    </div>
  );
};

export default LabResults;
