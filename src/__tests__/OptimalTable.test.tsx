import { fireEvent, render, screen } from '@testing-library/react';
import OptimalTable, {
  TableColumn,
  TableRow,
} from '../components/OptimalTable';

// Example data based on the hypertension food data
const sampleColumns: TableColumn[] = [
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
    key: 'allergy',
    header: 'Allergy Risk',
    type: 'boolean',
    editable: true,
  },
];

const sampleData: TableRow[] = [
  {
    id: '1',
    food: 'Oats',
    sodium_mg: 2,
    potassium_mg: 429,
    fiber_g: 10.6,
    allergy: false,
  },
  {
    id: '2',
    food: 'Salmon',
    sodium_mg: 59,
    potassium_mg: 628,
    fiber_g: 0,
    allergy: false,
  },
  {
    id: '3',
    food: 'Almonds',
    sodium_mg: 1,
    potassium_mg: 705,
    fiber_g: 12.5,
    allergy: true,
  },
];

describe('OptimalTable Component', () => {
  const mockOnDataChange = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('renders table with correct columns and data', () => {
    render(
      <OptimalTable
        columns={sampleColumns}
        data={sampleData}
        title="Food Nutrition Data"
        onDataChange={mockOnDataChange}
      />
    );

    // Check title
    expect(screen.getByText('Food Nutrition Data')).toBeInTheDocument();

    // Check column headers
    expect(screen.getByText('Food Item')).toBeInTheDocument();
    expect(screen.getByText('Sodium')).toBeInTheDocument();
    expect(screen.getByText('Potassium')).toBeInTheDocument();
    expect(screen.getByText('Fiber')).toBeInTheDocument();
    expect(screen.getByText('Allergy Risk')).toBeInTheDocument();

    // Check data
    expect(screen.getByDisplayValue('Oats')).toBeInTheDocument();
    expect(screen.getByDisplayValue('2')).toBeInTheDocument();
    expect(screen.getByDisplayValue('429')).toBeInTheDocument();
  });

  it('allows editing text fields', async () => {
    render(
      <OptimalTable
        columns={sampleColumns}
        data={sampleData}
        onDataChange={mockOnDataChange}
      />
    );

    const foodInput = screen.getByDisplayValue('Oats');
    fireEvent.change(foodInput, { target: { value: 'Steel Cut Oats' } });

    expect(mockOnDataChange).toHaveBeenCalledWith(
      expect.arrayContaining([
        expect.objectContaining({
          id: '1',
          food: 'Steel Cut Oats',
        }),
      ])
    );
  });

  it('allows editing number fields', async () => {
    render(
      <OptimalTable
        columns={sampleColumns}
        data={sampleData}
        onDataChange={mockOnDataChange}
      />
    );

    const sodiumInput = screen.getByDisplayValue('2');
    fireEvent.change(sodiumInput, { target: { value: '5' } });

    expect(mockOnDataChange).toHaveBeenCalledWith(
      expect.arrayContaining([
        expect.objectContaining({
          id: '1',
          sodium_mg: 5,
        }),
      ])
    );
  });

  it('allows editing boolean fields', async () => {
    render(
      <OptimalTable
        columns={sampleColumns}
        data={sampleData}
        onDataChange={mockOnDataChange}
      />
    );

    // Find the first checkbox (allergy field for the first row)
    const allergyCheckboxes = screen.getAllByRole('checkbox');
    const firstCheckbox = allergyCheckboxes[0];
    fireEvent.click(firstCheckbox);

    expect(mockOnDataChange).toHaveBeenCalledWith(
      expect.arrayContaining([
        expect.objectContaining({
          id: '1',
          allergy: true,
        }),
      ])
    );
  });

  it('allows adding new rows', async () => {
    render(
      <OptimalTable
        columns={sampleColumns}
        data={sampleData}
        onDataChange={mockOnDataChange}
      />
    );

    const addButton = screen.getByText('Add Row');
    fireEvent.click(addButton);

    expect(mockOnDataChange).toHaveBeenCalledWith(
      expect.arrayContaining([
        expect.objectContaining({
          food: '',
          sodium_mg: 0,
          potassium_mg: 0,
          fiber_g: 0,
          allergy: false,
        }),
      ])
    );
  });

  it('allows deleting rows', async () => {
    render(
      <OptimalTable
        columns={sampleColumns}
        data={sampleData}
        onDataChange={mockOnDataChange}
      />
    );

    const deleteButtons = screen.getAllByTitle('Delete row');
    fireEvent.click(deleteButtons[0]);

    expect(mockOnDataChange).toHaveBeenCalledWith(
      expect.arrayContaining([
        expect.objectContaining({ id: '2' }),
        expect.objectContaining({ id: '3' }),
      ])
    );
  });

  it('respects maxRows limit', () => {
    render(
      <OptimalTable
        columns={sampleColumns}
        data={sampleData}
        onDataChange={mockOnDataChange}
        maxRows={3}
      />
    );

    // Should show warning since we're at max rows
    expect(
      screen.getByText('Maximum number of rows (3) reached.')
    ).toBeInTheDocument();
  });

  it('shows units in headers', () => {
    render(
      <OptimalTable
        columns={sampleColumns}
        data={sampleData}
        onDataChange={mockOnDataChange}
      />
    );

    // Use getAllByText to get all instances and check that they exist
    const mgUnits = screen.getAllByText('(mg)');
    const gUnits = screen.getAllByText('(g)');
    
    expect(mgUnits.length).toBeGreaterThan(0);
    expect(gUnits.length).toBeGreaterThan(0);
    
    // Verify that units appear in headers (not just in table cells)
    const headers = screen.getAllByRole('columnheader');
    const headerText = headers.map(header => header.textContent).join(' ');
    expect(headerText).toContain('(mg)');
    expect(headerText).toContain('(g)');
  });

  it('handles non-editable columns', () => {
    const nonEditableColumns = sampleColumns.map(col => ({
      ...col,
      editable: false,
    }));

    render(
      <OptimalTable
        columns={nonEditableColumns}
        data={sampleData}
        onDataChange={mockOnDataChange}
      />
    );

    // Should show values as text, not inputs
    expect(screen.getByText('Oats')).toBeInTheDocument();
    expect(screen.getByText('2')).toBeInTheDocument();
  });
});
