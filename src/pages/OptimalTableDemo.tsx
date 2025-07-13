import React, { useState } from 'react';
import OptimalTable, {
  TableColumn,
  TableRow,
} from '../components/OptimalTable';

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
