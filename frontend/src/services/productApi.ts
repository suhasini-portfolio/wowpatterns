import type { Product } from "../types/product";

const API_URL = import.meta.env.VITE_API_URL;

function mapProduct(data: any): Product {
  return {
    id: data.product_id,
    name: data.product_title,
    price: Number(data.price),
  };
}

export async function getProducts(): Promise<Product[]> {
  const response = await fetch(`${API_URL}/products/`);

  if (!response.ok) {
    throw new Error("Failed to fetch products");
  }

  const data = await response.json();

  return data.map(mapProduct);
}

export async function getProduct(id: number): Promise<Product> {
  const response = await fetch(`${API_URL}/products/${id}`);

  if (!response.ok) {
    throw new Error("Failed to fetch product");
  }

  const data = await response.json();

  return mapProduct(data);
}