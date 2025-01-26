import './styles.css'; // Import global styles
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CartPage from "./pages/CartPage"; // Import the CartPage component

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
