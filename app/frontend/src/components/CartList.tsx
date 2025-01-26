import React, { useEffect } from "react";
import { useCart } from "../context/CartContext";

const CartDisplay: React.FC = () => {
  const { cart, fetchCart } = useCart();

  useEffect(() => {
    fetchCart();
  }, [fetchCart]);

  return (
    <div className="card">
      <h3>Your Cart</h3>
      {cart.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <ul>
          {cart.map((item) => (
            <li key={item.item}>
              {item.quantity} × {item.item} @ {item.discounted_price.toFixed(2)} €
              <span style={{ color: "gray", fontSize: "0.9rem" }}>
                {" "}
                (Original: {item.original_price.toFixed(2)} €)
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CartDisplay;
