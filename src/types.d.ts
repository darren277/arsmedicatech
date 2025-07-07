export interface PatientType {
  first_name?: string;
  last_name?: string;
  demographic_no?: string;
  date_of_birth?: string;
  sex?: string;
  phone?: string;
  email?: string;
  location?: string[] | null;
  history: any[];
}
