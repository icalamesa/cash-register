import React from "react";
import CatalogList from "../components/CatalogList";
import AddToCart from "../components/AddProduct";
import CartList from "../components/CartList";
import CartClear from "../components/ClearCartButton";
import Offers from "../components/OfferPane";

const CartPage: React.FC = () => {
  return (
    <div className="container">
      {/* Left Column */}
      <div className="column">
        <div className="card">
          <Offers />
        </div>
        <div className="card">
          <h2>Catalog</h2>
          <CatalogList />
        </div>
      </div>

      {/* Right Column */}
      <div className="column">
        <div className="card">
          <h2>Your Cart</h2>

          <AddToCart />
        </div>
        <div className="card">
          <h2>Add to Cart</h2>
          <CartList />
        </div>
      </div>
    </div>
  );
};

export default CartPage;
