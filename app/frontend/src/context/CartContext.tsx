import React, { createContext, useContext, useState } from "react";

interface CartItem {
  code: string;
  quantity: number;
  original_price: number;
  discounted_price: number;
}

interface CartContextType {
  cart: CartItem[];
  addToCart: (item: CartItem) => void;
  clearCart: () => void;
  fetchCart: () => Promise<void>;
}

const CartContext = createContext<CartContextType | undefined>(undefined);

export const CartProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [cart, setCart] = useState<CartItem[]>([]);

  const fetchCart = async () => {
    const response = await fetch("http://127.0.0.1:8000/cart/list");
    const data = await response.json();
    setCart(data.items);
  };

  const addToCart = async (item: { code: string; quantity: number }) => {
    await fetch("http://127.0.0.1:8000/cart/add", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(item),
    });
    await fetchCart(); // Update local cart state
  };

  const clearCart = async () => {
    await fetch("http://127.0.0.1:8000/cart/clear", {
      method: "POST",
    });
    setCart([]);
  };

  return (
    <CartContext.Provider value={{ cart, addToCart, clearCart, fetchCart }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) throw new Error("useCart must be used within a CartProvider");
  return context;
};
