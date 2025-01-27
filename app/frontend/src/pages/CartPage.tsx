import React from "react";
import Header from "../components/Header"; // Assuming Header is in the components folder
import Offers from "../components/OfferPane";
import CatalogList from "../components/CatalogList";
import AddToCart from "../components/AddProduct";
import CartList from "../components/CartList";

const CartPage: React.FC = () => {
  return (
    <>
      <Header /> {/* Header outside the container */}
      <div className="container">
        {/* Left Column */}
        <div className="column">
          <div className="card">
          <h2>Special Offers</h2>
            <Offers />
          </div>
          <div className="card">
            <h2>Catalog</h2>
            <h3>All available products.</h3>
            <CatalogList />
          </div>
        </div>

        {/* Right Column */}
        <div className="column">
          <div className="card">
            <h2>Add to Cart</h2>
            <AddToCart />
          </div>
          <div className="card">
            <h2>Cart</h2>
            <CartList />
          </div>
        </div>
      </div>
    </>
  );
};

export default CartPage;
