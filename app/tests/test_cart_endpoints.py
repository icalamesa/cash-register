# app/tests/test_cart_endpoints.py
import unittest
from fastapi.testclient import TestClient
from app.main import create_app

class TestCartEndpoints(unittest.TestCase):
    def setUp(self):
        """
        Re-initialize the FastAPI test client before each test.
        This ensures we start with a fresh state if your app or cart resets on startup.
        """
        self.app = create_app()
        self.client = TestClient(self.app)

    def test_add_valid_product(self):
        """
        Test adding a valid product to the cart via the endpoint.
        Expected: 200 OK and a confirmation message.
        """
        response = self.client.post("/cart/add", json={"item": "GR1", "quantity": 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Added 1 of GR1 to the cart"})

    def test_add_invalid_product(self):
        """
        Test adding an invalid product to the cart.
        Expected: 400 error with 'detail' key in the JSON response.
        """
        response = self.client.post("/cart/add", json={"item": "INVALID", "quantity": 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_add_invalid_quantity_string(self):
        """
        Test adding a product with a non-integer quantity (string).
        Expected: 422 error due to Pydantic validation (if using a Pydantic model).
        """
        response = self.client.post("/cart/add", json={"item": "GR1", "quantity": "INVALID"})
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())

    def test_add_empty_code(self):
        """
        Test adding a product with an empty code.
        Expected: 400 error with 'detail' key in the JSON response.
        """
        response = self.client.post("/cart/add", json={"item": "", "quantity": 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_add_negative_quantity(self):
        """
        Test adding a product with a negative quantity.
        Expected: 400 error with 'detail' key in the JSON response.
        """
        response = self.client.post("/cart/add", json={"item": "GR1", "quantity": -1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_list_cart_when_empty(self):
        """
        Test listing products in the cart when it's empty.
        Expected: 200 OK and an empty array.
        """
        response = self.client.get("/cart/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_list_cart_single_product(self):
        """
        Test listing products in the cart when there's only one product.
        Expected: 200 OK and a single-item array.
        """
        self.client.post("/cart/add", json={"item": "GR1", "quantity": 1})
        response = self.client.get("/cart/list")
        self.assertEqual(response.status_code, 200)
        expected_cart = [
            {"item": "GR1", "quantity": 1},
        ]
        self.assertEqual(response.json(), expected_cart)

    def test_list_cart_multiple_products(self):
        """
        Test listing products in the cart when multiple products have been added.
        Expected: 200 OK and an array with all items.
        """
        self.client.post("/cart/add", json={"item": "GR1", "quantity": 2})
        self.client.post("/cart/add", json={"item": "CF1", "quantity": 3})
        response = self.client.get("/cart/list")
        self.assertEqual(response.status_code, 200)
        expected_cart = [
            {"item": "GR1", "quantity": 2},
            {"item": "CF1", "quantity": 3},
        ]
        self.assertEqual(response.json(), expected_cart)

    def test_clear_cart_endpoint(self):
        """
        Test clearing the cart via the endpoint.
        Expected: 200 OK and an empty cart afterward.
        """
        self.client.post("/cart/add", json={"item": "GR1", "quantity": 2})
        self.client.post("/cart/add", json={"item": "SR1", "quantity": 3})

        response_clear = self.client.post("/cart/clear")
        self.assertEqual(response_clear.status_code, 200)
        self.assertIn("message", response_clear.json())

        response_list = self.client.get("/cart/list")
        self.assertEqual(response_list.status_code, 200)
        self.assertEqual(response_list.json(), [])

if __name__ == "__main__":
    unittest.main()
