import React from "react";
import AddProduct from "../components/AddProduct";
import CartList from "../components/CartList";
import ClearCartButton from "../components/ClearCartButton";

const HomePage: React.FC = () => {
  return (
    <div>
      <h1>Welcome to Cash Register</h1>
      <AddProduct />
      <CartList />
      <ClearCartButton />
    </div>
  );
};

export default HomePage;
