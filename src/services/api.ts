import API_URL from '../env_vars';
import authService from './auth';

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
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    return headers;
  }

  // Generic request method
  async request(endpoint: string, options: RequestInit = {}): Promise<any> {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      headers: this.getHeaders(),
      ...options,
    };

    try {
      const response = await fetch(url, config);
      const data = await response.json();

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
    return this.request('/api' + endpoint, {
      method: 'POST',
      body: JSON.stringify(data),
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

  // Patient-related API calls
  async getPatients() {
    return this.getAPI('/patients');
  }

  async searchPatients(query: string): Promise<any> {
    return this.getAPI(`/patients/search?q=${encodeURIComponent(query)}`);
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
  async getLLMChatHistory(): Promise<any> {
    return this.getAPI('/llm_chat');
  }

  async sendLLMMessage(prompt: string): Promise<any> {
    return this.postAPI('/llm_chat', { prompt });
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

  // Test endpoints
  async testSurrealDB(): Promise<any> {
    return this.getAPI('/test_surrealdb');
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

export default apiService;
