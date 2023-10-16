import axios from 'axios';

const baseURL = `http://localhost:8000`


const api = axios.create({
    baseURL,
    headers: {
        'Content-Type': 'application/json'
    },
    withCredentials: true
})

export default api;