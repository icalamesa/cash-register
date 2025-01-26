import React, { useEffect } from "react";
import { useCart } from "../context/CartContext";

const CartDisplay: React.FC = () => {
  const { cart, fetchCart } = useCart();

  useEffect(() => {
    fetchCart(); // Fetch the cart on component mount
  }, []);

  return (
    <div>
      <h2>Your Cart</h2>
      <ul>
        {cart.map((item) => (
          <li key={item.code}>
            {item.quantity} x {item.code} - ${item.discounted_price.toFixed(2)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CartDisplay;
