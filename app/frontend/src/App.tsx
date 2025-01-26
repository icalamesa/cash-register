import './styles.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CatalogList from "./components/CatalogList";
import AddToCart from "./components/AddProduct";
import CartList from "./components/CartList";
import CartClear from "./components/ClearCartButton";

const CartPage: React.FC = () => {
  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px", padding: "20px" }}>
      {/* Left Column: Catalog and Add to Cart */}
      <div>
        <h2>Catalog</h2>
        <CatalogList />
        <h2>Add to Cart</h2>
        <AddToCart />
      </div>

      {/* Right Column: Cart Items and Clear Cart */}
      <div>
        <h2>Cart</h2>
        <CartList />
        <CartClear />
      </div>
    </div>
  );
};

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CartPage />} />
      </Routes>
    </Router>
  );
};

export default App;
