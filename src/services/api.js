import API_URL from '../env_vars';
import authService from './auth';

class ApiService {
    constructor() {
        this.baseURL = API_URL;
    }

    // Helper method to get headers with authentication
    getHeaders() {
        const headers = {
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
    async request(endpoint, options = {}) {
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
    async get(endpoint) {
        return this.request(endpoint, { method: 'GET' });
    }

    // POST request
    async post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data),
        });
    }

    // PUT request
    async put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
    }

    // DELETE request
    async delete(endpoint) {
        return this.request(endpoint, { method: 'DELETE' });
    }

    // Patient-related API calls
    async getPatients() {
        return this.get('/patients');
    }

    async searchPatients(query) {
        return this.get(`/patients/search?q=${encodeURIComponent(query)}`);
    }

    async getPatient(patientId) {
        return this.get(`/patients/${patientId}`);
    }

    // Chat-related API calls
    async getChatHistory() {
        return this.get('/chat');
    }

    async sendChatMessage(message) {
        return this.post('/chat', { message });
    }

    // LLM-related API calls
    async getLLMChatHistory() {
        return this.get('/llm_chat');
    }

    async sendLLMMessage(prompt) {
        return this.post('/llm_chat', { prompt });
    }

    async resetLLMChat() {
        return this.post('/llm_chat/reset');
    }

    // Time API
    async getCurrentTime() {
        return this.get('/time');
    }

    // Admin-related API calls (require admin role)
    async getAllUsers() {
        return this.get('/admin/users');
    }

    async deactivateUser(userId) {
        return this.post(`/admin/users/${userId}/deactivate`);
    }

    async activateUser(userId) {
        return this.post(`/admin/users/${userId}/activate`);
    }

    async setupDefaultAdmin() {
        return this.post('/admin/setup');
    }

    // Test endpoints
    async testSurrealDB() {
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
    getById: (id) => apiService.get(`/patients/${id}`),
    
    // Create a new patient
    create: (patientData) => apiService.post('/patients', patientData),
    
    // Update a patient
    update: (id, patientData) => apiService.put(`/patients/${id}`, patientData),
    
    // Delete a patient
    delete: (id) => apiService.delete(`/patients/${id}`),
    
    // Search patients
    search: (query) => apiService.get(`/patients/search?q=${encodeURIComponent(query)}`)
};

export default apiService;
