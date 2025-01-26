import React from "react";
import CartList from "../components/CartList";
import CatalogList from "../components/CatalogList";
import AddToCart from "../components/AddProduct";
import CartClear from "../components/ClearCartButton";

const CartPage: React.FC = () => {
    return (
      <div className="container grid">
        <div>
          <h2>Catalog</h2>
          <CatalogList />
          <h2>Add to Cart</h2>
          <AddToCart />
        </div>
        <div>
          <h2>Your Cart</h2>
          <CartList />
          <CartClear />
        </div>
      </div>
    );
  };
  
  export default CartPage;
  