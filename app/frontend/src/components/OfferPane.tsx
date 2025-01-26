import React from "react";

const Offers: React.FC = () => {
  return (
    <div className="offers-card">
      <h2>Special Offers</h2>
      <ul className="offers-list">
        <li className="offer-item">
          <strong>Buy-One-Get-One-Free:</strong> On <em>Green Tea (GR1)</em>. Every second tea is free!
        </li>
        <li className="offer-item">
          <strong>Bulk Discount:</strong> Buy 3 or more <em>Strawberries (SR1)</em>, and the price drops to 4.50€ each.
        </li>
        <li className="offer-item">
          <strong>Coffee Lover's Discount:</strong> Buy 3 or more <em>Coffees (CF1)</em>, and each coffee is 2/3 of the original price.
        </li>
      </ul>
    </div>
  );
};

export default Offers;
