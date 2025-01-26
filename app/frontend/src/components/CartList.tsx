import React, { useEffect, useState } from "react";
import { listCart } from "../api/cart";

const CartList: React.FC = () => {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    const fetchCart = async () => {
      try {
        const response = await listCart();
        setCartItems(response.items);
      } catch (error) {
        console.error("Error fetching cart items:", error);
      }
    };

    fetchCart();
  }, []);

  if (!cartItems.length) return <p>Your cart is empty.</p>;

  return (
    <div>
      <h3>Cart Items</h3>
      <ul>
        {cartItems.map((item, index) => (
          <li key={index}>
            {item.item} - Quantity: {item.quantity} - Original: ${item.original_price} - Discounted: ${item.discounted_price}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CartList;
