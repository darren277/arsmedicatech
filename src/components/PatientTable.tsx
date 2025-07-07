import {
  flexRender,
  getCoreRowModel,
  useReactTable,
} from '@tanstack/react-table';
import React from 'react';

/*
interface Patient {
  id: string;
  first_name: string;
  last_name: string;
  highlighted_note: string;
}
*/

/** Dumb presentational component */
export function PatientTable({
  rows,
  isLoading = false,
  // }: {
  //     rows: Patient[];
  //     isLoading?: boolean;
}) {
  /** Column definition only runs once */
  //const columns = React.useMemo<ColumnDef<Patient>[]>(
  const columns = React.useMemo(
    () => [
      { accessorKey: 'first_name', header: 'First name' },
      { accessorKey: 'last_name', header: 'Last name' },
      {
        accessorKey: 'highlighted_note',
        header: 'Snippet',
        //cell: ctx => (<div dangerouslySetInnerHTML={{__html: ctx.getValue() as string,}} />),
        cell: ctx => (
          <div dangerouslySetInnerHTML={{ __html: ctx.getValue() }} />
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
          <tr key={row.id}>
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
