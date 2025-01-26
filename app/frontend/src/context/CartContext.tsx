import React, { createContext, useContext, useState, useCallback } from "react";
import { listCart, clearCart } from "../api/cart";

type CartContextType = {
  cart: { item: string; quantity: number; original_price: number; discounted_price: number }[];
  fetchCart: () => Promise<void>;
  notifyCartChange: () => void;
};

const CartContext = createContext<CartContextType | undefined>(undefined);

export const CartProvider: React.FC = ({ children }) => {
  const [cart, setCart] = useState<
    { item: string; quantity: number; original_price: number; discounted_price: number }[]
  >([]);

  const fetchCart = useCallback(async () => {
    const data = await listCart();
    setCart(data.items);
  }, []);

  const notifyCartChange = () => {
    fetchCart(); // Re-fetch the cart whenever this is called
  };

  return (
    <CartContext.Provider value={{ cart, fetchCart, notifyCartChange }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error("useCart must be used within a CartProvider");
  }
  return context;
};
