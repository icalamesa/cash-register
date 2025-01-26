import axios from "axios";
import { ListCartResponse, AddProductResponse, CartResponse } from "./types";

const API_BASE_URL = "http://127.0.0.1:8000";

export const addToCart = async (product: { code: string; quantity: number }): Promise<AddProductResponse> => {
  const response = await axios.post(`${API_BASE_URL}/cart/add`, product);
  return response.data;
};

export const listCart = async (): Promise<ListCartResponse> => {
  const response = await axios.get(`${API_BASE_URL}/cart/list`);
  return response.data;
};

export const clearCart = async (): Promise<CartResponse> => {
  const response = await axios.post(`${API_BASE_URL}/cart/clear`);
  return response.data;
};
