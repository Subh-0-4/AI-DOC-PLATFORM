import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export function setAuthToken(token) {
  if (token) {
    // ✅ use the REAL token here
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    // remove header when logged out
    delete api.defaults.headers.common["Authorization"];
  }
}

export default api;
