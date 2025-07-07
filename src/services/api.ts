import API_URL from '../env_vars';
import authService from './auth';

class ApiService {
  baseURL: string;

  constructor() {
    this.baseURL = API_URL;
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

  // POST request
  async post(endpoint: string, data: any): Promise<any> {
    return this.request(endpoint, {
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

  // DELETE request
  async delete(endpoint: string): Promise<any> {
    return this.request(endpoint, { method: 'DELETE' });
  }

  // Patient-related API calls
  async getPatients() {
    return this.get('/patients');
  }

  async searchPatients(query: string): Promise<any> {
    return this.get(`/patients/search?q=${encodeURIComponent(query)}`);
  }

  async getPatient(patientId: string): Promise<any> {
    return this.get(`/patients/${patientId}`);
  }

  // Chat-related API calls
  async getChatHistory(): Promise<any> {
    return this.get('/chat');
  }

  async sendChatMessage(message: string): Promise<any> {
    return this.post('/chat', { message });
  }

  // LLM-related API calls
  async getLLMChatHistory(): Promise<any> {
    return this.get('/llm_chat');
  }

  async sendLLMMessage(prompt: string): Promise<any> {
    return this.post('/llm_chat', { prompt });
  }

  async resetLLMChat(): Promise<any> {
    return this.post('/llm_chat/reset', {});
  }

  // Time API
  async getCurrentTime(): Promise<any> {
    return this.get('/time');
  }

  // Admin-related API calls (require admin role)
  async getAllUsers(): Promise<any> {
    return this.get('/admin/users');
  }

  async deactivateUser(userId: string): Promise<any> {
    return this.post(`/admin/users/${userId}/deactivate`, {});
  }

  async activateUser(userId: string): Promise<any> {
    return this.post(`/admin/users/${userId}/activate`, {});
  }

  async setupDefaultAdmin(): Promise<any> {
    return this.post('/admin/setup', {});
  }

  // Test endpoints
  async testSurrealDB(): Promise<any> {
    return this.get('/test_surrealdb');
  }
}

// Create a singleton instance
const apiService = new ApiService();

// Patient CRUD operations
export const patientAPI = {
  // Get all patients
  getAll: () => apiService.get('/patients'),

  // Get a specific patient
  getById: (id: string) => apiService.get(`/patients/${id}`),

  // Create a new patient
  create: (patientData: any) => apiService.post('/patients', patientData),

  // Update a patient
  update: (id: string, patientData: any) =>
    apiService.put(`/patients/${id}`, patientData),

  // Delete a patient
  delete: (id: string) => apiService.delete(`/patients/${id}`),

  // Search patients
  search: (query: string) =>
    apiService.get(`/patients/search?q=${encodeURIComponent(query)}`),
};

export default apiService;
