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

export interface Conversation {
  id: number | string;
  name: string;
  lastMessage: string;
  avatar: string;
  messages: { sender: string; text: string }[];
  participantId?: string;
  isAI?: boolean;
}

export interface EncounterType {
  note_id?: string;
  date_created?: string;
  provider_id?: string;
  note_text?: string;
  diagnostic_codes?: string[];
  status?: string;
  patient?: PatientType;
  score?: number;
  highlighted_note?: string;
}

export interface SOAPNotesType {
  subjective?: string;
  objective?: string;
  assessment?: string;
  plan?: string;
}
