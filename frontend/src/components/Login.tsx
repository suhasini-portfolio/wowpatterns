import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  loginCustomer,
  getCurrentCustomer,
} from "../services/customerApi";
import type { Customer } from "../types/customer";
import CustomerProfile from "./CustomerProfile";

function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [customer, setCustomer] = useState<Customer | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      return;
    }

    const loadCustomer = async () => {
      try {
        const profile = await getCurrentCustomer(token);
        setCustomer(profile);
      } catch (error) {
        localStorage.removeItem("access_token");
        setCustomer(null);
      }
    };

    loadCustomer();
  }, []);

  const handleLogin = async () => {
    setError("");
    setCustomer(null);
      try {
        const data = await loginCustomer(email, password);
        console.log("Login response:", data);
        localStorage.setItem("access_token", data.access_token);
        const profile = await getCurrentCustomer(data.access_token);
        setCustomer(profile);
        navigate("/profile");
      } catch (error) {
          if (error instanceof Error) {
            setError(error.message);
          } else {
            setError("Unable to connect to server");
          }
      }
  };
  const handleLogout = () => {
    localStorage.removeItem("access_token");
    setCustomer(null);
  };

  return (
    <div>
      <h2>Customer Login</h2>

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
      />

      <br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(event) => setPassword(event.target.value)}
      />

      <br />
      {error && <p>{error}</p>}
      <button type="button" onClick={handleLogin}>
        Login
      </button>
      {customer && (
        <div>
            <CustomerProfile customer={customer} onLogout={handleLogout} />
        </div>
        )}
    </div>
  );
}

export default Login;