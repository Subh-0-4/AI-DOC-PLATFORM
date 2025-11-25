import axios from "axios";

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "https://ai-doc-platform-1.onrender.com",
  // In production (Vercel): REACT_APP_API_URL is set → calls that
  // Locally: if env is missing, it falls back to Render backend
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
