import React, { useEffect } from "react";
import { useCart } from "../context/CartContext";

const CartDisplay: React.FC = () => {
  const { cart, fetchCart } = useCart();

  useEffect(() => {
    fetchCart();
  }, [fetchCart]);

  return (
    <div className="card cart-container">
      {cart.length === 0 ? (
        <p className="empty-cart-message">Your cart is empty.</p>
      ) : (
        <ul className="cart-list">
          {cart.map((item) => (
            <li key={item.item} className="cart-item">
              <div className="cart-item-details">
                <span className="cart-item-name">
                  {item.quantity} × {item.item}
                </span>
              </div>
              <div className="cart-item-price-container">
                {item.original_price !== item.discounted_price && (
                  <span className="cart-item-original">
                    {item.original_price.toFixed(2)} €
                  </span>
                )}
                <span className="cart-item-price">
                  {item.discounted_price.toFixed(2)} €
                </span>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CartDisplay;
