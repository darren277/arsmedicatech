import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  //baseURL: process.env.REACT_APP_API_URL,
});

export default api;
