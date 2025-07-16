import { API_URL } from '../env_vars';
import authService from './auth';
import logger from './logging';

class ApiService {
  baseURL: string;
  apiURL: string;

  constructor() {
    this.baseURL = API_URL;
    this.apiURL = API_URL + '/api';
  }

  // Helper method to get headers with authentication
  getHeaders() {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    // Add auth token if available
    const token = authService.getToken();
    logger.debug('API getHeaders - token available:', !!token);
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
      logger.debug('API getHeaders - Authorization header set');
    } else {
      logger.debug('API getHeaders - No token available');
    }

    return headers;
  }

  // Generic request method
  async request(endpoint: string, options: RequestInit = {}): Promise<any> {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      headers: this.getHeaders(),
      credentials: 'include' as RequestCredentials,
      ...options,
    };

    logger.debug('API request - URL:', url);
    logger.debug('API request - Method:', options.method || 'GET');
    logger.debug('API request - Headers:', config.headers);

    try {
      const response = await fetch(url, config);
      logger.debug('API request - Response status:', response.status);

      const data = await response.json();
      logger.debug('API request - Response data:', data);

      if (!response.ok) {
        // Handle authentication errors
        if (response.status === 401) {
          // Token might be expired, try to refresh or logout
          await authService.logout();
          throw new Error('Authentication required. Please log in again.');
        }
        throw new Error(data.error || `HTTP error! status: ${response.status}`);
      }

      return data;
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  // GET request
  async get(endpoint: string): Promise<any> {
    return this.request(endpoint, { method: 'GET' });
  }

  // GET request with API prefix
  async getAPI(endpoint: string): Promise<any> {
    return this.request('/api' + endpoint, { method: 'GET' });
  }

  // POST request
  async post(endpoint: string, data: any): Promise<any> {
    return this.request(endpoint, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  // POST request with API prefix
  async postAPI(endpoint: string, data: any): Promise<any> {
    // If data is FormData, do not stringify and do not set Content-Type
    const isFormData =
      typeof FormData !== 'undefined' && data instanceof FormData;
    let headers = this.getHeaders();
    if (isFormData) {
      // Remove Content-Type so browser sets it with boundary
      const { ['Content-Type']: _, ...rest } = headers;
      headers = rest;
    }
    return this.request('/api' + endpoint, {
      method: 'POST',
      body: isFormData ? data : JSON.stringify(data),
      headers,
    });
  }

  // PUT request
  async put(endpoint: string, data: any): Promise<any> {
    return this.request(endpoint, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  // PUT request with API prefix
  async putAPI(endpoint: string, data: any): Promise<any> {
    return this.request('/api' + endpoint, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  // DELETE request
  async delete(endpoint: string): Promise<any> {
    return this.request(endpoint, { method: 'DELETE' });
  }

  // DELETE request with API prefix
  async deleteAPI(endpoint: string): Promise<any> {
    return this.request('/api' + endpoint, { method: 'DELETE' });
  }

  // DELETE request with API prefix and body
  async deleteAPIWithBody(endpoint: string, data: any): Promise<any> {
    return this.request('/api' + endpoint, {
      method: 'DELETE',
      body: JSON.stringify(data),
    });
  }

  // Patient-related API calls
  async getPatients() {
    return this.getAPI('/patients');
  }

  async searchPatients(query: string): Promise<any> {
    return this.getAPI(`/patients/search?q=${encodeURIComponent(query)}`);
  }

  async searchEncounters(query: string): Promise<any> {
    return this.getAPI(`/encounters/search?q=${encodeURIComponent(query)}`);
  }

  async searchPatientsAndEncounters(query: string): Promise<any> {
    // Search both patients and encounters and combine results
    const [patientResults, encounterResults] = await Promise.all([
      this.searchPatients(query),
      this.searchEncounters(query),
    ]);

    // Combine and return results
    return [...(patientResults || []), ...(encounterResults || [])];
  }

  async getPatient(patientId: string): Promise<any> {
    return this.getAPI(`/patients/${patientId}`);
  }

  // Chat-related API calls
  async getChatHistory(): Promise<any> {
    return this.getAPI('/chat');
  }

  async sendChatMessage(message: string): Promise<any> {
    return this.postAPI('/chat', { message });
  }

  // LLM-related API calls
  async getLLMChatHistory(assistantId: string): Promise<any> {
    const allChats = await this.getAPI('/llm_chat');
    // Find the chat for this assistant
    return (
      allChats.find((chat: any) => chat.assistant_id === assistantId) || {
        messages: [],
      }
    );
  }

  async sendLLMMessage(assistantId: string, prompt: string): Promise<any> {
    return this.postAPI('/llm_chat', { assistant_id: assistantId, prompt });
  }

  async resetLLMChat(): Promise<any> {
    return this.postAPI('/llm_chat/reset', {});
  }

  // Time API
  async getCurrentTime(): Promise<any> {
    return this.getAPI('/time');
  }

  // Admin-related API calls (require admin role)
  async getAllUsers(): Promise<any> {
    return this.getAPI('/admin/users');
  }

  async deactivateUser(userId: string): Promise<any> {
    return this.postAPI(`/admin/users/${userId}/deactivate`, {});
  }

  async activateUser(userId: string): Promise<any> {
    return this.postAPI(`/admin/users/${userId}/activate`, {});
  }

  async setupDefaultAdmin(): Promise<any> {
    return this.postAPI('/admin/setup', {});
  }

  async checkUsersExist(): Promise<any> {
    return this.getAPI('/users/exist');
  }

  async searchUsers(query: string): Promise<any> {
    return this.getAPI(`/users/search?q=${encodeURIComponent(query)}`);
  }

  async getUserConversations(): Promise<any> {
    return this.getAPI('/conversations');
  }

  async getConversationMessages(conversationId: string): Promise<any> {
    return this.getAPI(`/conversations/${conversationId}/messages`);
  }

  async sendMessage(conversationId: string, text: string): Promise<any> {
    return this.postAPI(`/conversations/${conversationId}/messages`, { text });
  }

  async createConversation(
    participants: string[],
    type: string = 'user_to_user'
  ): Promise<any> {
    logger.debug('Creating conversation via API:', {
      participants,
      type,
    });
    const result = await this.postAPI('/conversations', { participants, type });
    logger.debug('Conversation creation API result:', result);
    return result;
  }

  // Test endpoints
  async testSurrealDB(): Promise<any> {
    return this.getAPI('/test_surrealdb');
  }

  // Lab Results API
  async getLabResults(): Promise<any> {
    return this.getAPI('/lab_results');
  }

  // Optimal Service API
  async callOptimal(tableData: any): Promise<any> {
    return this.postAPI('/optimal', { tableData });
  }
}

// Create a singleton instance
const apiService = new ApiService();

// Patient CRUD operations
export const patientAPI = {
  // Get all patients
  getAll: () => apiService.getAPI('/patients'),

  // Get a specific patient
  getById: (id: string) => apiService.getAPI(`/patients/${id}`),

  // Create a new patient
  create: (patientData: any) => apiService.postAPI('/patients', patientData),

  // Update a patient
  update: (id: string, patientData: any) =>
    apiService.putAPI(`/patients/${id}`, patientData),

  // Delete a patient
  delete: (id: string) => apiService.deleteAPI(`/patients/${id}`),

  // Search patients
  search: (query: string) =>
    apiService.getAPI(`/patients/search?q=${encodeURIComponent(query)}`),
};

// Encounter CRUD operations
export const encounterAPI = {
  // Get all encounters
  getAll: () => apiService.getAPI('/encounters'),

  // Get encounters for a specific patient
  getByPatient: (patientId: string) =>
    apiService.getAPI(`/patients/${patientId}/encounters`),

  // Get a specific encounter
  getById: (id: string) => apiService.getAPI(`/encounters/${id}`),

  // Create a new encounter for a patient
  create: (patientId: string, encounterData: any) =>
    apiService.postAPI(`/patients/${patientId}/encounters`, encounterData),

  // Update an encounter
  update: (id: string, encounterData: any) =>
    apiService.putAPI(`/encounters/${id}`, encounterData),

  // Delete an encounter
  delete: (id: string) => apiService.deleteAPI(`/encounters/${id}`),

  // Search encounters
  search: (query: string) =>
    apiService.getAPI(`/encounters/search?q=${encodeURIComponent(query)}`),
};

// Organization API operations
export const organizationAPI = {
  // Get all organizations
  getAll: () => apiService.getAPI('/organizations'),

  // Get a specific organization by ID
  getById: (id: string) => apiService.getAPI(`/organizations/${id}`),

  // Create a new organization
  create: (orgData: any) => apiService.postAPI('/organizations', orgData),

  // Update an organization
  update: (id: string, orgData: any) =>
    apiService.putAPI(`/organizations/${id}`, orgData),

  // Get all clinics for an organization
  getClinics: (orgId: string) =>
    apiService.getAPI(`/organizations/${orgId}/clinics`),

  // Add a clinic to an organization
  addClinic: (orgId: string, clinicId: string) =>
    apiService.postAPI(`/organizations/${orgId}/clinics`, {
      clinic_id: clinicId,
    }),

  // Remove a clinic from an organization
  removeClinic: (orgId: string, clinicId: string) =>
    apiService.deleteAPIWithBody(`/organizations/${orgId}/clinics`, {
      clinic_id: clinicId,
    }),
};

// Metrics API operations
export const metricsAPI = {
  // Get all metrics
  getAll: () => apiService.getAPI('/metrics'),

  // Get all metrics for a user
  getAllForUser: (userId: string) =>
    apiService.getAPI(`/metrics/users/${userId}`),

  // Get a specific metric by ID
  getById: (id: string) => apiService.getAPI(`/metrics/${id}`),

  // Create a new metric
  create: (metricData: any) => apiService.postAPI('/metrics', metricData),

  // Update a metric
  update: (id: string, metricData: any) =>
    apiService.putAPI(`/metrics/${id}`, metricData),

  // Delete a metric
  delete: (id: string) => apiService.deleteAPI(`/metrics/${id}`),

  // Get metrics for a user on a specific date
  getForUserByDate: (userId: string, date: string) =>
    apiService.getAPI(`/metrics/user/${userId}/date/${date}`),

  // Upsert (create or update) metrics for a user on a specific date
  upsertForUserByDate: (userId: string, date: string, metrics: any[]) =>
    apiService.postAPI(`/metrics/user/${userId}/date/${date}`, { metrics }),
};

// File upload API operations
export const fileUploadAPI = {
  // Get all uploads
  getAll: () => apiService.getAPI('/uploads'),
  // Get a specific upload by ID
  getById: (id: string) => apiService.getAPI(`/uploads/${id}`),

  // Create a new upload
  create: (uploadData: any) => apiService.postAPI('/uploads', uploadData),

  // Update an upload
  update: (id: string, uploadData: any) =>
    apiService.putAPI(`/uploads/${id}`, uploadData),

  // Delete an upload
  delete: (id: string) => apiService.deleteAPI(`/uploads/${id}`),
};

// Plugin API operations
export const pluginAPI = {
  // Get all plugins
  getAll: () => apiService.getAPI('/plugins'),
};

export default apiService;
