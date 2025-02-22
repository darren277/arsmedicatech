import axios from 'axios';

import API_URL from './env_vars'

const api = axios.create({
    //baseURL: 'http://127.0.0.1:5000',
    //baseURL: process.env.REACT_APP_API_URL,
    baseURL: API_URL
});

export default api;
