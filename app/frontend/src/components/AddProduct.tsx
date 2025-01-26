import React, { useEffect, useState } from "react";
import { useCart } from "../context/CartContext";
import { addToCart, clearCart } from "../api/cart";
import { getCatalog } from "../api/catalog";

const AddToCart: React.FC = () => {
  const [catalog, setCatalog] = useState<{ code: string; name: string }[]>([]);
  const [selectedProduct, setSelectedProduct] = useState("");
  const [quantity, setQuantity] = useState(1);
  const { notifyCartChange } = useCart();

  useEffect(() => {
    const fetchCatalog = async () => {
      try {
        const data = await getCatalog();
        setCatalog(data.items); // Assume the catalog API response has an 'items' array
      } catch (error) {
        console.error("Failed to fetch catalog", error);
        alert("Failed to load catalog. Please try again later.");
      }
    };

    fetchCatalog();
  }, []);

  const handleAddToCart = async () => {
    if (!selectedProduct || quantity < 1) {
      alert("Please select a valid product and quantity.");
      return;
    }

    const [code] = selectedProduct.split("-");
    try {
      await addToCart({ code, quantity });
      notifyCartChange(); // Notify cart change
    } catch (error) {
      console.error("Failed to add product to cart", error);
    }
  };

  const handleClearCart = async () => {
    try {
      const response = await clearCart();
      notifyCartChange();
      alert(response.message);
    } catch (error) {
      console.error("Failed to clear the cart", error);
      alert("Failed to clear cart. Please try again later.");
    }
  };

  return (
    <div className="card">
      <label className="block mb-1">Select a product:</label>
      <select
        value={selectedProduct}
        onChange={(e) => setSelectedProduct(e.target.value)}
        className="select"
      >
        <option value="">Select a product </option>
        {catalog.map((product) => (
          <option key={product.code} value={`${product.code}-${product.name}`}>
            {product.code} - {product.name}
          </option>
        ))}
      </select>
      <br />
      <label className="block mb-1">Quantity:</label>
      <input
        type="number"
        value={quantity}
        onChange={(e) => setQuantity(Number(e.target.value))}
        className="input"
        min={1}
      />

      {/* Flex container for buttons */}
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: "15px" }}>
        <button onClick={handleAddToCart} className="button">
          Add
        </button>
        <button onClick={handleClearCart} className="clear-cart-button">
          Clear Cart
        </button>
      </div>
    </div>
  );
};

export default AddToCart;
