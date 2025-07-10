import apiService from './api';

export interface Appointment {
  id: string;
  patient_id: string;
  provider_id: string;
  appointment_date: string;
  start_time: string;
  end_time: string;
  appointment_type: string;
  status: string;
  notes?: string;
  location?: string;
  created_at: string;
  updated_at: string;
}

export interface CreateAppointmentData {
  patient_id: string;
  provider_id?: string;
  appointment_date: string;
  start_time: string;
  end_time: string;
  appointment_type?: string;
  notes?: string;
  location?: string;
}

export interface UpdateAppointmentData {
  appointment_date?: string;
  start_time?: string;
  end_time?: string;
  appointment_type?: string;
  notes?: string;
  location?: string;
  status?: string;
}

export interface AvailableSlot {
  start_time: string;
  end_time: string;
}

export interface AppointmentType {
  value: string;
  label: string;
}

export interface AppointmentStatus {
  value: string;
  label: string;
}

class AppointmentService {
  private baseUrl = '/appointments';

  async getAppointments(params?: {
    date?: string;
    patient_id?: string;
    provider_id?: string;
    status?: string;
  }): Promise<{ appointments: Appointment[]; total: number }> {
    const queryParams = new URLSearchParams();
    if (params?.date) queryParams.append('date', params.date);
    if (params?.patient_id) queryParams.append('patient_id', params.patient_id);
    if (params?.provider_id)
      queryParams.append('provider_id', params.provider_id);
    if (params?.status) queryParams.append('status', params.status);

    const response = await apiService.getAPI(
      `${this.baseUrl}?${queryParams.toString()}`
    );
    return response;
  }

  async getAppointment(appointmentId: string): Promise<Appointment> {
    const response = await apiService.getAPI(
      `${this.baseUrl}/${appointmentId}`
    );
    return response.appointment;
  }

  async createAppointment(data: CreateAppointmentData): Promise<Appointment> {
    const response = await apiService.postAPI(this.baseUrl, data);
    return response.appointment;
  }

  async updateAppointment(
    appointmentId: string,
    data: UpdateAppointmentData
  ): Promise<void> {
    await apiService.putAPI(`${this.baseUrl}/${appointmentId}`, data);
  }

  async cancelAppointment(
    appointmentId: string,
    reason?: string
  ): Promise<void> {
    await apiService.postAPI(`${this.baseUrl}/${appointmentId}/cancel`, {
      reason,
    });
  }

  async confirmAppointment(appointmentId: string): Promise<void> {
    await apiService.postAPI(`${this.baseUrl}/${appointmentId}/confirm`);
  }

  async getAvailableSlots(
    date: string,
    providerId?: string,
    duration?: number
  ): Promise<AvailableSlot[]> {
    const queryParams = new URLSearchParams({ date });
    if (providerId) queryParams.append('provider_id', providerId);
    if (duration) queryParams.append('duration', duration.toString());

    const response = await apiService.getAPI(
      `${this.baseUrl}/available-slots?${queryParams.toString()}`
    );
    return response.available_slots;
  }

  async getAppointmentTypes(): Promise<AppointmentType[]> {
    const response = await apiService.getAPI(`${this.baseUrl}/types`);
    return response.appointment_types;
  }

  async getAppointmentStatuses(): Promise<AppointmentStatus[]> {
    const response = await apiService.getAPI(`${this.baseUrl}/statuses`);
    return response.appointment_statuses;
  }
}

export const appointmentService = new AppointmentService();
