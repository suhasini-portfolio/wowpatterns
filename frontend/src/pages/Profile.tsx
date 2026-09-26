import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import CustomerProfile from "../components/CustomerProfile";
import { getCurrentCustomer } from "../services/customerApi";
import type { Customer } from "../types/customer";

function Profile() {
  const [customer, setCustomer] = useState<Customer | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      navigate("/login");
      return;
    }

    const loadCustomer = async () => {
      try {
        const profile = await getCurrentCustomer(token);
        setCustomer(profile);
      } catch (error) {
        localStorage.removeItem("access_token");
        navigate("/login");
      }
    };

    loadCustomer();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    navigate("/login");
  };

  if (!customer) {
    return <p>Loading...</p>;
  }

  return (
    <CustomerProfile
      customer={customer}
      onLogout={handleLogout}
    />
  );
}

export default Profile;