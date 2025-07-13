import React, { useState } from 'react';
import OptimalTable, {
  TableColumn,
  TableRow,
} from '../components/OptimalTable';
import apiService from '../services/api';

const OptimalTableDemo: React.FC = () => {
  // Define the columns based on your hypertension data structure
  const columns: TableColumn[] = [
    {
      key: 'food',
      header: 'Food Item',
      type: 'text',
      editable: true,
    },
    {
      key: 'sodium_mg',
      header: 'Sodium',
      type: 'number',
      editable: true,
      unit: 'mg',
      min: 0,
      max: 1000,
    },
    {
      key: 'potassium_mg',
      header: 'Potassium',
      type: 'number',
      editable: true,
      unit: 'mg',
      min: 0,
      max: 2000,
    },
    {
      key: 'fiber_g',
      header: 'Fiber',
      type: 'number',
      editable: true,
      unit: 'g',
      min: 0,
      max: 50,
    },
    {
      key: 'saturated_fat_g',
      header: 'Saturated Fat',
      type: 'number',
      editable: true,
      unit: 'g',
      min: 0,
      max: 50,
    },
    {
      key: 'calories',
      header: 'Calories',
      type: 'number',
      editable: true,
      unit: 'kcal',
      min: 0,
      max: 1000,
    },
    {
      key: 'allergy',
      header: 'Allergy Risk',
      type: 'boolean',
      editable: true,
    },
  ];

  // Initial data based on your hypertension.py example
  const initialData: TableRow[] = [
    {
      id: '1',
      food: 'Oats',
      sodium_mg: 2,
      potassium_mg: 429,
      fiber_g: 10.6,
      saturated_fat_g: 1.1,
      calories: 389,
      allergy: false,
    },
    {
      id: '2',
      food: 'Salmon',
      sodium_mg: 59,
      potassium_mg: 628,
      fiber_g: 0,
      saturated_fat_g: 1.0,
      calories: 208,
      allergy: false,
    },
    {
      id: '3',
      food: 'Spinach',
      sodium_mg: 79,
      potassium_mg: 558,
      fiber_g: 2.2,
      saturated_fat_g: 0,
      calories: 23,
      allergy: false,
    },
    {
      id: '4',
      food: 'Banana',
      sodium_mg: 1,
      potassium_mg: 358,
      fiber_g: 2.6,
      saturated_fat_g: 0.1,
      calories: 89,
      allergy: false,
    },
    {
      id: '5',
      food: 'Almonds',
      sodium_mg: 1,
      potassium_mg: 705,
      fiber_g: 12.5,
      saturated_fat_g: 3.8,
      calories: 579,
      allergy: true,
    },
  ];

  const [tableData, setTableData] = useState<TableRow[]>(initialData);
  const [isProcessing, setIsProcessing] = useState(false);
  const [optimalResult, setOptimalResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const handleDataChange = (newData: TableRow[]) => {
    setTableData(newData);
    console.log('Table data updated:', newData);
  };

  const handleExportData = () => {
    const csvContent = [
      // Header row
      columns.map(col => col.header).join(','),
      // Data rows
      ...tableData.map(row => columns.map(col => row[col.key]).join(',')),
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'food_nutrition_data.csv';
    a.click();
    window.URL.revokeObjectURL(url);
  };

  const handleResetData = () => {
    setTableData(initialData);
    setOptimalResult(null);
    setError(null);
  };

  const handleProcessWithOptimal = async () => {
    setIsProcessing(true);
    setError(null);
    setOptimalResult(null);

    try {
      const result = await apiService.callOptimal(tableData);
      setOptimalResult(result);
      console.log('Optimal service result:', result);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : 'Failed to process with Optimal service'
      );
      console.error('Error calling Optimal service:', err);
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Optimal Table Demo
          </h1>
          <p className="text-lg text-gray-600 max-w-3xl">
            Dynamic table component for managing nutritional data. Edit values,
            add/remove rows, and export data.
          </p>
        </div>

        <div className="mb-6 flex space-x-4">
          <button
            onClick={handleExportData}
            className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors duration-200 font-medium"
          >
            Export CSV
          </button>
          <button
            onClick={handleResetData}
            className="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition-colors duration-200 font-medium"
          >
            Reset Data
          </button>
          <button
            onClick={handleProcessWithOptimal}
            disabled={isProcessing}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-blue-400 disabled:cursor-not-allowed transition-colors duration-200 font-medium"
          >
            {isProcessing ? 'Processing...' : 'Process with Optimal'}
          </button>
        </div>

        <OptimalTable
          columns={columns}
          data={tableData}
          title="Food Nutrition Data"
          onDataChange={handleDataChange}
          showAddRow={true}
          showDeleteRow={true}
          maxRows={20}
          className="mb-8"
        />

        {/* Error Display */}
        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 rounded-lg p-4">
            <div className="flex">
              <div className="flex-shrink-0">
                <svg
                  className="h-5 w-5 text-red-400"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>
              <div className="ml-3">
                <h3 className="text-sm font-medium text-red-800">Error</h3>
                <div className="mt-2 text-sm text-red-700">{error}</div>
              </div>
            </div>
          </div>
        )}

        {/* Optimal Results Display */}
        {optimalResult && (
          <div className="mb-6 bg-green-50 border border-green-200 rounded-lg p-6">
            <h3 className="text-lg font-semibold text-green-800 mb-4">
              Optimal Service Results
            </h3>
            <div className="space-y-4">
              {optimalResult.result && (
                <div>
                  <h4 className="text-md font-medium text-green-700 mb-2">
                    Optimization Results:
                  </h4>
                  <div className="bg-white rounded-lg p-4 border border-green-200">
                    <div className="grid grid-cols-2 gap-4 text-sm">
                      <div>
                        <span className="font-medium">Status:</span>{' '}
                        {optimalResult.result.status}
                      </div>
                      {optimalResult.result.fun && (
                        <div>
                          <span className="font-medium">Objective Value:</span>{' '}
                          {optimalResult.result.fun.toFixed(4)}
                        </div>
                      )}
                      {optimalResult.result.nit && (
                        <div>
                          <span className="font-medium">Iterations:</span>{' '}
                          {optimalResult.result.nit}
                        </div>
                      )}
                    </div>
                    {optimalResult.result.x && (
                      <div className="mt-4">
                        <h5 className="font-medium text-green-700 mb-2">
                          Optimal Servings:
                        </h5>
                        <div className="bg-gray-50 rounded p-3">
                          <pre className="text-sm overflow-auto">
                            {JSON.stringify(optimalResult.result.x, null, 2)}
                          </pre>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}
              <div>
                <h4 className="text-md font-medium text-green-700 mb-2">
                  Processed Data:
                </h4>
                <pre className="bg-white rounded-lg p-4 border border-green-200 overflow-auto text-sm">
                  {JSON.stringify(optimalResult.tableData, null, 2)}
                </pre>
              </div>
            </div>
          </div>
        )}

        <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
          <h3 className="text-lg font-semibold text-gray-800 mb-4">
            Current Data
          </h3>
          <pre className="bg-gray-50 p-4 rounded-lg overflow-auto text-sm">
            {JSON.stringify(tableData, null, 2)}
          </pre>
        </div>
      </div>
    </div>
  );
};

export default OptimalTableDemo;
