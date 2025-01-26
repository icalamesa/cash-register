import React from "react";
import CartList from "../components/CartList";

const CartPage: React.FC = () => {
  return (
    <div>
      <h1>Your Cart</h1>
      <CartList />
    </div>
  );
};

export default CartPage;
