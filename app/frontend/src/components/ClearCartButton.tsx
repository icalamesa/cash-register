import React from "react";
import { clearCart } from "../api/cart";
import { useCart } from "../context/CartContext";

const ClearCartButton: React.FC = () => {
  const { notifyCartChange } = useCart();
  const handleClear = async () => {
    try {
      const response = await clearCart();
      notifyCartChange(); 
      alert(response.message);
    } catch (error) {
      alert("Failed to clear cart.");
    }
  };
  

  return <button onClick={handleClear}>Clear Cart</button>;
};

export default ClearCartButton;
