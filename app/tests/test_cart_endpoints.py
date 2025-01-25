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
        self.product_data = {
            "GR1": 3.11,  # Green Tea
            "SR1": 5.00,  # Strawberries
            "CF1": 11.23  # Coffee
        }

    def test_add_valid_product(self):
        response = self.client.post("/cart/add", json={"code": "GR1", "quantity": 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Added 1 of GR1 to the cart"})

    def test_add_invalid_product(self):
        response = self.client.post("/cart/add", json={"code": "INVALID", "quantity": 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_add_invalid_quantity_string(self):
        response = self.client.post("/cart/add", json={"code": "GR1", "quantity": "INVALID"})
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())

    def test_add_empty_code(self):
        response = self.client.post("/cart/add", json={"code": "", "quantity": 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_add_negative_quantity(self):
        response = self.client.post("/cart/add", json={"code": "GR1", "quantity": -1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_list_cart_when_empty(self):
        response = self.client.get("/cart/list")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), {"items": []})

    def test_list_cart_single_product(self):
        self.client.post("/cart/add", json={"code": "GR1", "quantity": 1})

        response = self.client.get("/cart/list")
        self.assertEqual(response.status_code, 200)

        expected_cart = {
            "items": [
                {
                    "item": "GR1",
                    "quantity": 1,
                    "original_price": self.product_data["GR1"],
                    "discounted_price": self.product_data["GR1"]
                }
            ]
        }
        self.assertEqual(response.json(), expected_cart)

    def test_list_cart_multiple_products(self):
        self.client.post("/cart/add", json={"code": "GR1", "quantity": 1})
        self.client.post("/cart/add", json={"code": "CF1", "quantity": 1})

        response = self.client.get("/cart/list")
        self.assertEqual(response.status_code, 200)

        expected_cart = {
            "items": [
                {
                    "item": "GR1",
                    "quantity": 1,
                    "original_price": self.product_data["GR1"],
                    "discounted_price": self.product_data["GR1"]
                },
                {
                    "item": "CF1",
                    "quantity": 1,
                    "original_price": self.product_data["CF1"],
                    "discounted_price": self.product_data["CF1"]
                }
            ]
        }
        self.assertEqual(response.json(), expected_cart)

    def test_clear_cart_endpoint(self):
        self.client.post("/cart/add", json={"code": "GR1", "quantity": 2})
        self.client.post("/cart/add", json={"code": "SR1", "quantity": 3})

        response_clear = self.client.post("/cart/clear")
        self.assertEqual(response_clear.status_code, 200)
        self.assertEqual(response_clear.json(), {"message": "Cart cleared"})

        response_list = self.client.get("/cart/list")
        self.assertEqual(response_list.status_code, 200)
        self.assertEqual(response_list.json(), {"items": []})


if __name__ == "__main__":
    unittest.main()
