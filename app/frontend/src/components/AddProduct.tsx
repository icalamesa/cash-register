import React, { useEffect, useState } from "react";
import { getCatalog } from "../api/catalog";
import { addToCart } from "../api/cart";

const AddToCart: React.FC = () => {
  const [catalog, setCatalog] = useState<{ code: string; name: string }[]>([]);
  const [selectedProduct, setSelectedProduct] = useState("");
  const [quantity, setQuantity] = useState(1);

  useEffect(() => {
    const fetchCatalog = async () => {
      try {
        const data = await getCatalog();
        console.log("Catalog fetched:", data);
        setCatalog(data.items || []);
      } catch (error) {
        console.error("Failed to fetch catalog:", error);
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
      console.log("Adding to cart:", { code, quantity });
      await addToCart({code, quantity});
      alert("Product added to cart!");
    } catch (error) {
      console.error("Failed to add product to cart:", error);
      alert("Failed to add product. Please try again.");
    }
  };

  return (
    <div>
      <h2>Add to Cart</h2>
      <select
        value={selectedProduct}
        onChange={(e) => setSelectedProduct(e.target.value)}
        disabled={catalog.length === 0}
      >
        <option value="">Select a product</option>
        {catalog.map((item) => (
          <option key={item.code} value={`${item.code}-${item.name}`}>
            {item.code} - {item.name}
          </option>
        ))}
      </select>
      {catalog.length === 0 && <p>Loading catalog...</p>}
      <input
        type="number"
        value={quantity}
        min={1}
        onChange={(e) => setQuantity(Number(e.target.value))}
      />
      <button onClick={handleAddToCart}>Add</button>
    </div>
  );
};

export default AddToCart;
