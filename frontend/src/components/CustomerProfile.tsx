import type { Customer } from "../types/customer";

type CustomerProfileProps = {
  customer: Customer;
  onLogout: () => void;
};

function CustomerProfile({
  customer,
  onLogout,
}: CustomerProfileProps) {
  return (
    <div>
      <h2>Welcome, {customer.full_name}</h2>

      <p>Email: {customer.email}</p>

      <p>Customer Code: {customer.customer_code}</p>

      <button type="button" onClick={onLogout}>
        Logout
      </button>
    </div>
  );
}

export default CustomerProfile;