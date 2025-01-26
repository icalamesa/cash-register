import React, { useEffect, useState } from "react";
import { getCatalog } from "../api/catalog";

const CatalogList: React.FC = () => {
  const [catalog, setCatalog] = useState<{ code: string; name: string; price: number }[]>([]);

  useEffect(() => {
    const fetchCatalog = async () => {
      try {
        const data = await getCatalog();
        setCatalog(data.items);
      } catch (error) {
        console.error("Failed to fetch catalog", error);
      }
    };

    fetchCatalog();
  }, []);

  return (
    <div>
      <h2>Catalog</h2>
      <table>
        <thead>
          <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Price (€)</th>
          </tr>
        </thead>
        <tbody>
          {catalog.map((item) => (
            <tr key={item.code}>
              <td>{item.code}</td>
              <td>{item.name}</td>
              <td>{item.price.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CatalogList;
