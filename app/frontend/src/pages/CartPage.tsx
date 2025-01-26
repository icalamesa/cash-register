import React from "react";
import CartList from "../components/CartList";
import CatalogList from "../components/CatalogList";
import AddToCart from "../components/AddProduct";
import CartClear from "../components/ClearCartButton";

const CartPage: React.FC = () => {
    return (
      <div className="container">
        {/* Left Column */}
        <div className="column">
          <div className="card">
            <h2>Catalog</h2>
            <CatalogList />
          </div>
          <div className="card">
            <h2>Add to Cart</h2>
            <AddToCart />
          </div>
        </div>
  
        {/* Right Column */}
        <div className="column">
          <div className="card">
            <h2>Your Cart</h2>
            <CartList />
          </div>
          <div className="card">
            <CartClear />
          </div>
        </div>
      </div>
    );
  };
  
  export default CartPage;