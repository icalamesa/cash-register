import React, { useEffect, useState } from "react";
import { getCatalog } from "../api/catalog";

const CatalogList: React.FC = () => {
    const products = [
      { code: "GR1", name: "Green Tea", price: 3.11 },
      { code: "SR1", name: "Strawberries", price: 5.0 },
      { code: "CF1", name: "Coffee", price: 11.23 },
    ];
  
    return (
      <div className="card">
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
      </div>
    );
  };
  
  export default CatalogList;
  