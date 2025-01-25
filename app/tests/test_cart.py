import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestAddToCart(unittest.TestCase):
    def test_add_valid(self):
        """
        Test adding a valid product to the cart.
        Expected: Successful addition with a confirmation message.
        """
        client = TestClient(app)
        response = client.post("/cart/add", json={"item": "GR1", "quantity": 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Added 1 of GR1 to the cart"})

    def test_add_invalid_product(self):
        """
        Test adding an invalid product to the cart.
        Expected: 400 error with appropriate message.
        """
        client = TestClient(app)
        response = client.post("/cart/add", json={"item": "INVALID", "quantity": 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_add_invalid_quantity(self):
        """
        Test adding a product with a negative quantity.
        Expected: 400 error with appropriate message.
        """
        client = TestClient(app)
        response = client.post("/cart/add", json={"item": "GR1", "quantity": "INVALID"})
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())

    def test_add_empty_code(self):
        """
        Test adding a product with an empty code.
        Expected: 400 error with appropriate message.
        """
        client = TestClient(app)
        response = client.post("/cart/add", json={"item": "", "quantity": 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_add_negative_quantity(self):
        """
        Test adding a product with a negative quantity.
        Expected: 400 error with appropriate message.
        """
        client = TestClient(app)
        response = client.post("/cart/add", json={"item": "GR1", "quantity": -1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

if __name__ == "__main__":
    unittest.main()
