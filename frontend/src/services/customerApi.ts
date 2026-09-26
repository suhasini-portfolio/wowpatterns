import type { Customer, LoginResponse } from "../types/customer";
const API_URL = import.meta.env.VITE_API_URL;
export async function loginCustomer(
  email: string,
  password: string
): Promise<LoginResponse> {
  console.log("Login email:", email);
  console.log("Login password:", password);
  const response = await fetch(
    `${API_URL}/customers/login`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email,
        password,
      }),
    }
  );

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail);
  }

  return response.json();
}

export async function getCurrentCustomer(token: string): Promise<Customer> {
  const response = await fetch(
    `${API_URL}/customers/me`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (!response.ok) {
    throw new Error("Unable to load customer");
  }

  return response.json();
}