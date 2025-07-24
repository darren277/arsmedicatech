import React, { useEffect, useState } from 'react';

export interface TableColumn {
  key: string;
  header: string;
  type: 'text' | 'number' | 'boolean';
  editable?: boolean;
  min?: number;
  max?: number;
  step?: number;
  unit?: string;
}

export interface TableRow {
  id: string;
  [key: string]: any;
}

interface OptimalTableProps {
  columns: TableColumn[];
  data: TableRow[];
  title?: string;
  onDataChange?: (newData: TableRow[]) => void;
  showAddRow?: boolean;
  showDeleteRow?: boolean;
  maxRows?: number;
  className?: string;
}

const OptimalTable: React.FC<OptimalTableProps> = ({
  columns,
  data,
  title,
  onDataChange,
  showAddRow = true,
  showDeleteRow = true,
  maxRows,
  className = '',
}) => {
  const [tableData, setTableData] = useState<TableRow[]>(data);
  const [editingCell, setEditingCell] = useState<{
    rowId: string;
    columnKey: string;
  } | null>(null);

  // Update internal state when props change
  useEffect(() => {
    setTableData(data);
  }, [data]);

  const handleCellChange = (rowId: string, columnKey: string, value: any) => {
    const newData = tableData.map(row =>
      row.id === rowId ? { ...row, [columnKey]: value } : row
    );
    setTableData(newData);
    onDataChange?.(newData);
  };

  const handleAddRow = () => {
    if (maxRows && tableData.length >= maxRows) return;

    const newRow: TableRow = {
      id: `row-${Date.now()}-${Math.random()}`,
      ...Object.fromEntries(
        columns.map(col => [
          col.key,
          col.type === 'boolean' ? false : col.type === 'number' ? 0 : '',
        ])
      ),
    };

    const newData = [...tableData, newRow];
    setTableData(newData);
    onDataChange?.(newData);
  };

  const handleDeleteRow = (rowId: string) => {
    const newData = tableData.filter(row => row.id !== rowId);
    setTableData(newData);
    onDataChange?.(newData);
  };

  const renderCell = (row: TableRow, column: TableColumn) => {
    const value = row[column.key];
    const isEditing =
      editingCell?.rowId === row.id && editingCell?.columnKey === column.key;

    if (!column.editable) {
      return (
        <div className="px-3 py-2 text-sm text-gray-700">
          {column.type === 'boolean' ? (
            <span
              className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                value
                  ? 'bg-green-100 text-green-800'
                  : 'bg-gray-100 text-gray-800'
              }`}
            >
              {value ? 'Yes' : 'No'}
            </span>
          ) : (
            <>
              {value}
              {column.unit && (
                <span className="text-gray-500 ml-1">{column.unit}</span>
              )}
            </>
          )}
        </div>
      );
    }

    switch (column.type) {
      case 'boolean':
        return (
          <div className="px-3 py-2">
            <input
              type="checkbox"
              checked={value || false}
              onChange={e =>
                handleCellChange(row.id, column.key, e.target.checked)
              }
              className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"
            />
          </div>
        );

      case 'number':
        return (
          <div className="px-3 py-2">
            <input
              type="number"
              value={value || ''}
              onChange={e =>
                handleCellChange(
                  row.id,
                  column.key,
                  parseFloat(e.target.value) || 0
                )
              }
              min={column.min}
              max={column.max}
              step={column.step || 1}
              className="w-full px-2 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              onFocus={() =>
                setEditingCell({ rowId: row.id, columnKey: column.key })
              }
              onBlur={() => setEditingCell(null)}
            />
            {column.unit && (
              <span className="text-xs text-gray-500 ml-1">{column.unit}</span>
            )}
          </div>
        );

      case 'text':
      default:
        return (
          <div className="px-3 py-2">
            <input
              type="text"
              value={value || ''}
              onChange={e =>
                handleCellChange(row.id, column.key, e.target.value)
              }
              className="w-full px-2 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              onFocus={() =>
                setEditingCell({ rowId: row.id, columnKey: column.key })
              }
              onBlur={() => setEditingCell(null)}
            />
          </div>
        );
    }
  };

  return (
    <div
      className={`bg-white rounded-xl shadow-lg border border-gray-200 ${className}`}
    >
      {title && (
        <div className="px-6 py-4 border-b border-gray-200">
          <h3 className="text-lg font-semibold text-gray-800">{title}</h3>
        </div>
      )}

      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gradient-to-r from-gray-50 to-gray-100">
            <tr>
              {columns.map(column => (
                <th
                  key={column.key}
                  className="px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider"
                >
                  <div className="flex items-center space-x-1">
                    <span>{column.header}</span>
                    {column.unit && (
                      <span className="text-xs text-gray-400 font-normal">
                        ({column.unit})
                      </span>
                    )}
                  </div>
                </th>
              ))}
              {showDeleteRow && (
                <th className="px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                  Actions
                </th>
              )}
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-100">
            {tableData.map(row => (
              <tr
                key={row.id}
                className="hover:bg-gray-50 transition-colors duration-150"
              >
                {columns.map(column => (
                  <td
                    key={`${row.id}-${column.key}`}
                    className="whitespace-nowrap"
                  >
                    {renderCell(row, column)}
                  </td>
                ))}
                {showDeleteRow && (
                  <td className="px-6 py-4 whitespace-nowrap">
                    <button
                      onClick={() => handleDeleteRow(row.id)}
                      className="text-red-600 hover:text-red-900 transition-colors duration-200"
                      title="Delete row"
                    >
                      <svg
                        className="w-5 h-5"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                        />
                      </svg>
                    </button>
                  </td>
                )}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {showAddRow && (!maxRows || tableData.length < maxRows) && (
        <div className="px-6 py-4 border-t border-gray-200 bg-gray-50">
          <button
            onClick={handleAddRow}
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200"
          >
            <svg
              className="w-4 h-4 mr-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 6v6m0 0v6m0-6h6m-6 0H6"
              />
            </svg>
            Add Row
          </button>
        </div>
      )}

      {maxRows && tableData.length >= maxRows && (
        <div className="px-6 py-3 bg-yellow-50 border-t border-yellow-200">
          <p className="text-sm text-yellow-700">
            Maximum number of rows ({maxRows}) reached.
          </p>
        </div>
      )}
    </div>
  );
};

export default OptimalTable;
