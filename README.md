# **Cash Register API**

A **FastAPI-based project** for managing a shopping cart with dynamic pricing rules, product catalog management, and  API documentation.

---

## **Key Features**
- **Dynamic Pricing Engine**:
  - **BOGO**: Buy-one-get-one-free for **Green Tea (GR1)**.
  - **Bulk Discounts**: Price drop for **Strawberries (SR1)** if 3 or more are purchased.
  - **Conditional Discounts**: Price reduction for **Coffee (CF1)** when buying 3 or more.
- **Real-Time Cart Management**:
  - Add, list, and clear cart items dynamically.
- **Interactive API Documentation**:
  - Swagger UI and ReDoc auto-generated documentation.
- **CI/CD Integration**:
  - Automated deployment of API documentation to GitHub Pages via GitHub Actions.
- **Comprehensive Testing**:
  - Unit and endpoint tests for all features.

---

## **Project Structure**
```
cash-register/
├── app/
│   ├── main.py             # FastAPI app entry point
│   ├── cart.py             # Cart functionality
│   ├── catalog.py          # Product catalog logic
│   ├── pricing_engine.py   # Pricing rules and logic
│   ├── models.py           # Pydantic request/response models
│   └── tests/              # Unit and integration tests
├── openapi.json            # Auto-generated API schema
├── requirements.txt        # Dependencies
└── .github/workflows/      # CI/CD workflows
```

---

## **API Endpoints**
### **1. Add Product to Cart**
- **POST** `/cart/add`
  ```json
  {
    "code": "GR1",
    "quantity": 2
  }
  ```
  **Response**:
  ```json
  { "message": "Added 2 of GR1 to the cart" }
  ```

### **2. List Products in Cart**
- **GET** `/cart/list`
  **Response**:
  ```json
  {
    "items": [
      {
        "item": "GR1",
        "quantity": 2,
        "original_price": 6.22,
        "discounted_price": 3.11
      }
    ]
  }
  ```

### **3. Clear Cart**
- **POST** `/cart/clear`
  **Response**:
  ```json
  { "message": "Cart cleared" }
  ```

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/cash-register.git
   cd cash-register
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   uvicorn app.main:create_app --reload --factory
   ```
5. Access the docs:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## **Run Tests**
Run the test suite:
```bash
pytest --cov=app
```

---

## **Deployment**
GitHub Actions workflow automates:
1. Generating `openapi.json`.
2. Building and deploying Swagger UI documentation to GitHub Pages.

Access the live documentation:
```
https://icalamesa.github.io/cash-register/
```

---

## **License**
Licensed under the MIT License. See [LICENSE](LICENSE).

---

### **Contact**
- **Email**: contact@icalamesa.com
- **GitHub**: [https://github.com/icalamesa](https://github.com/icalamesa)

---
