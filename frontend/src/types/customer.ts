export type Customer = {
  customer_id: number;
  customer_code: string;
  full_name: string;
  email: string;
  mobile_country_id: number | null;
  mobile_country_code: number | null;
  mobile: string | null;
  is_active: boolean;
};
export type LoginResponse = {
  access_token: string;
  token_type: string;
};