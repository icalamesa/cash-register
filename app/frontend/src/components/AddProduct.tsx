import React, { useState } from "react";
import { useCart } from "../context/CartContext";

const AddProduct: React.FC = () => {
  const { addToCart } = useCart();
  const [code, setCode] = useState("");
  const [quantity, setQuantity] = useState(1);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await addToCart({ code, quantity });
    setCode("");
    setQuantity(1);
  };

  return (
    <form onSubmit={handleSubmit}>
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
        onChange={(e) => setQuantity(parseInt(e.target.value, 10))}
      />
      <button type="submit">Add to Cart</button>
    </form>
  );
};

export default AddProduct;
