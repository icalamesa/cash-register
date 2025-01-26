import React, { useState } from "react";
import { useCart } from "../context/CartContext";
import { addToCart } from "../api/cart";

const AddToCart: React.FC = () => {
  const [selectedProduct, setSelectedProduct] = useState("");
  const [quantity, setQuantity] = useState(1);
  const { notifyCartChange } = useCart();

  const handleAddToCart = async () => {
    if (!selectedProduct || quantity < 1) {
      alert("Please select a valid product and quantity.");
      return;
    }

    const [code] = selectedProduct.split("-");
    try {
      await addToCart({ code, quantity });
      notifyCartChange(); // Notify cart change
      alert("Product added to cart!");
    } catch (error) {
      console.error("Failed to add product to cart", error);
      alert("Failed to add product. Please try again.");
    }
  };

  return (
    <div className="card">
      <label>Select a product:</label>
      <select
        value={selectedProduct}
        onChange={(e) => setSelectedProduct(e.target.value)}
        className="select"
      >
        <option value="">Select a product</option>
        <option value="GR1">Green Tea</option>
        <option value="SR1">Strawberries</option>
        <option value="CF1">Coffee</option>
      </select>

      <label>Quantity:</label>
      <input
        type="number"
        value={quantity}
        onChange={(e) => setQuantity(Number(e.target.value))}
        className="input"
      />

      <button onClick={handleAddToCart} className="button">
        Add
      </button>
    </div>
  );
};

export default AddToCart;