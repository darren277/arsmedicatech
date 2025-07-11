import {
  flexRender,
  getCoreRowModel,
  useReactTable,
} from '@tanstack/react-table';
import React from 'react';
import { EncounterType, PatientType } from '../types';

/** Dumb presentational component for search results */
export function SearchResultsTable({
  rows,
  isLoading = false,
  onRowClick,
}: {
  rows: (PatientType | EncounterType)[];
  isLoading?: boolean;
  onRowClick?: (item: PatientType | EncounterType) => void;
}) {
  /** Column definition only runs once */
  const columns = React.useMemo(
    () => [
      {
        id: 'patient_name',
        header: 'Patient Name',
        cell: (ctx: any) => {
          const item = ctx.row.original;
          // Handle both patient and encounter search results
          if ('patient' in item && item.patient) {
            // This is an encounter result
            return (
              `${item.patient.first_name || ''} ${item.patient.last_name || ''}`.trim() ||
              '-'
            );
          } else {
            // This is a direct patient result
            return (
              `${item.first_name || ''} ${item.last_name || ''}`.trim() || '-'
            );
          }
        },
      },
      {
        id: 'patient_dob',
        header: 'Date of Birth',
        cell: (ctx: any) => {
          const item = ctx.row.original;
          let dob = null;

          if ('patient' in item && item.patient) {
            // This is an encounter result
            dob = item.patient.date_of_birth;
          } else {
            // This is a direct patient result
            dob = item.date_of_birth;
          }

          return dob ? new Date(dob).toLocaleDateString() : '-';
        },
      },
      {
        id: 'visit_date',
        header: 'Visit Date',
        cell: (ctx: any) => {
          const item = ctx.row.original;
          // Only show visit date for encounter results
          if ('date_created' in item) {
            return item.date_created
              ? new Date(item.date_created).toLocaleDateString()
              : '-';
          }
          return '-';
        },
      },
      {
        accessorKey: 'highlighted_note',
        header: 'Snippet',
        cell: (ctx: any): JSX.Element => (
          <div dangerouslySetInnerHTML={{ __html: ctx.getValue() || '' }} />
        ),
      },
    ],
    []
  );

  const table = useReactTable({
    data: rows,
    columns,
    getCoreRowModel: getCoreRowModel(),
  });

  if (isLoading) {
    return <p className="p-4">Loading…</p>;
  }

  return (
    <table className="min-w-full text-sm">
      <thead className="bg-gray-50 text-left font-semibold">
        {table.getHeaderGroups().map(hg => (
          <tr key={hg.id}>
            {hg.headers.map(header => (
              <th key={header.id} className="px-4 py-2">
                {flexRender(
                  header.column.columnDef.header,
                  header.getContext()
                )}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody className="divide-y divide-gray-200">
        {table.getRowModel().rows.map(row => (
          <tr
            key={row.id}
            className={`hover:bg-gray-50 ${onRowClick ? 'cursor-pointer' : ''}`}
            onClick={() => onRowClick && onRowClick(row.original)}
          >
            {row.getVisibleCells().map(cell => (
              <td key={cell.id} className="px-4 py-2">
                {flexRender(cell.column.columnDef.cell, cell.getContext())}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

/** Patient table component for displaying patient data with CRUD actions */
export function PatientTable({
  patients,
  isLoading = false,
  onEdit,
  onDelete,
  onView,
  onRowClick,
}: {
  patients: PatientType[];
  isLoading?: boolean;
  onEdit?: (patient: PatientType) => void;
  onDelete?: (patient: PatientType) => void;
  onView?: (patient: PatientType) => void;
  onRowClick?: (patient: PatientType) => void;
}) {
  const columns = React.useMemo(
    () => [
      { accessorKey: 'demographic_no', header: 'ID' },
      { accessorKey: 'first_name', header: 'First Name' },
      { accessorKey: 'last_name', header: 'Last Name' },
      {
        accessorKey: 'date_of_birth',
        header: 'Date of Birth',
        cell: (ctx: any) => {
          const value = ctx.getValue();
          return value ? new Date(value).toLocaleDateString() : '-';
        },
      },
      { accessorKey: 'phone', header: 'Phone' },
      { accessorKey: 'email', header: 'Email' },
      {
        id: 'actions',
        header: 'Actions',
        cell: (ctx: any) => {
          const patient = ctx.row.original;
          return (
            <div className="flex space-x-2">
              {onView && (
                <button
                  onClick={e => {
                    e.stopPropagation();
                    onView(patient);
                  }}
                  className="px-3 py-1 text-sm bg-blue-500 text-white rounded hover:bg-blue-600"
                >
                  View
                </button>
              )}
              {onEdit && (
                <button
                  onClick={e => {
                    e.stopPropagation();
                    onEdit(patient);
                  }}
                  className="px-3 py-1 text-sm bg-yellow-500 text-white rounded hover:bg-yellow-600"
                >
                  Edit
                </button>
              )}
              {onDelete && (
                <button
                  onClick={e => {
                    e.stopPropagation();
                    onDelete(patient);
                  }}
                  className="px-3 py-1 text-sm bg-red-500 text-white rounded hover:bg-red-600"
                >
                  Delete
                </button>
              )}
            </div>
          );
        },
      },
    ],
    [onEdit, onDelete, onView]
  );

  const table = useReactTable({
    data: patients,
    columns,
    getCoreRowModel: getCoreRowModel(),
  });

  if (isLoading) {
    return <p className="p-4">Loading patients...</p>;
  }

  if (!patients || patients.length === 0) {
    return <p className="p-4 text-gray-500">No patients found.</p>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          {table.getHeaderGroups().map(headerGroup => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map(header => (
                <th
                  key={header.id}
                  className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  {flexRender(
                    header.column.columnDef.header,
                    header.getContext()
                  )}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {table.getRowModel().rows.map(row => (
            <tr
              key={row.id}
              className={`hover:bg-gray-50 ${onRowClick ? 'cursor-pointer' : ''}`}
              onClick={() => onRowClick && onRowClick(row.original)}
            >
              {row.getVisibleCells().map(cell => (
                <td
                  key={cell.id}
                  className="px-6 py-4 whitespace-nowrap text-sm text-gray-900"
                >
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
