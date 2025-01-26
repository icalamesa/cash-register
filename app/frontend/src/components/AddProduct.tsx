import React, { useState } from "react";
import { addToCart } from "../api/cart";

const AddProduct: React.FC = () => {
  const [code, setCode] = useState("");
  const [quantity, setQuantity] = useState(0);

  const handleAdd = async () => {
    try {
      const response = await addToCart({ code, quantity });
      alert(response.message);
    } catch (error) {
      alert("Failed to add product to cart.");
    }
  };

  return (
    <div>
      <h3>Add Product</h3>
      <input
        type="text"
        placeholder="Product Code"
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />
      <input
        type="number"
        placeholder="Quantity"
        value={quantity}
        onChange={(e) => setQuantity(parseInt(e.target.value))}
      />
      <button onClick={handleAdd}>Add to Cart</button>
    </div>
  );
};

export default AddProduct;
