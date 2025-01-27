import React from "react";
import { FaShoppingCart } from "react-icons/fa";
import "../styles.css";

const Header: React.FC = () => {
  return (
    <header className="header">
      <h1 className="header-title">Shopping Cart App</h1>
      {/*<button className="cart-button">
        <FaShoppingCart />
      </button>*/}
    </header>
  );
};

export default Header;
