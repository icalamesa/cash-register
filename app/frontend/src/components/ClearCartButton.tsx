import React from "react";
import { clearCart } from "../api/cart";

const ClearCartButton: React.FC = () => {
  const handleClear = async () => {
    try {
      const response = await clearCart();
      alert(response.message);
    } catch (error) {
      alert("Failed to clear cart.");
    }
  };

  return <button onClick={handleClear}>Clear Cart</button>;
};

export default ClearCartButton;
