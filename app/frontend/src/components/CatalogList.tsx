import React, { useEffect, useState } from "react";
import { getCatalog } from "../api/catalog";

const CatalogList: React.FC = () => {
  const [products, setProducts] = useState<{ code: string; name: string; price: number }[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCatalog = async () => {
      try {
        const data = await getCatalog();
        setProducts(data.items);
        setLoading(false);
      } catch (err) {
        console.error("Failed to fetch catalog", err);
        setError("Failed to load catalog. Please try again later.");
        setLoading(false);
      }
    };

    fetchCatalog();
  }, []);

  if (loading) {
    return <p>Loading catalog...</p>;
  }

  if (error) {
    return <p className="error">{error}</p>;
  }

  return (
    <table className="table">
      <thead>
        <tr>
          <th>Code</th>
          <th>Name</th>
          <th>Price (€)</th>
        </tr>
      </thead>
      <tbody>
        {products.map((product) => (
          <tr key={product.code}>
            <td>{product.code}</td>
            <td>{product.name}</td>
            <td>{product.price.toFixed(2)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default CatalogList;
