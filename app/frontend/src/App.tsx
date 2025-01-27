import './styles.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CartPage from "./pages/CartPage";

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
