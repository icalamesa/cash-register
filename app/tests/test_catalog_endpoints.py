import unittest
from fastapi.testclient import TestClient
from app.main import create_app

class TestCatalogEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = TestClient(self.app)
        self.catalog_data = {
            "GR1": {"name": "Green Tea", "original_price": 3.11},
            "SR1": {"name": "Strawberries", "original_price": 5.00},
            "CF1": {"name": "Coffee", "original_price": 11.23},
        }

    def test_list_catalog_success(self):
        """
        Test retrieving the full catalog from the endpoint.
        Expected: 200 OK with the correct list of catalog items.
        """
        response = self.client.get("/catalog/list")
        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        self.assertIn("items", response_json)
        items = response_json["items"]
        self.assertIsInstance(items, list)

        expected_items = [
            {"item": "GR1", "name": "Green Tea", "original_price": 3.11},
            {"item": "SR1", "name": "Strawberries", "original_price": 5.00},
            {"item": "CF1", "name": "Coffee", "original_price": 11.23},
        ]
        self.assertEqual(items, expected_items)


if __name__ == "__main__":
    unittest.main()
