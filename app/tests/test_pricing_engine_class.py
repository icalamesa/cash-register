import unittest
from app.pricing_engine import PricingEngine

class TestPricingEngine(unittest.TestCase):
    def setUp(self):
        """
        Set up minimal product data for testing. Each product code maps to its base price.
        """
        self.product_data = {
            "GR1": 3.11,  # Green Tea
            "SR1": 5.00,  # Strawberries
            "CF1": 11.23  # Coffee
        }

    def test_case_1(self):
        """
        Basket: GR1, GR1
        Consolidation: GR1 -> 2
        Expected total: 3.11
        """
        items = [
            {"item": "GR1", "quantity": 2}
        ]
        total = PricingEngine.calculate_total(items, self.product_data)
        self.assertEqual(total, 3.11)

    def test_case_2(self):
        """
        Basket: SR1, SR1, GR1, SR1
        Consolidation: SR1 -> 3, GR1 -> 1
        Expected total: 16.61
        """
        items = [
            {"item": "SR1", "quantity": 3},
            {"item": "GR1", "quantity": 1}
        ]
        total = PricingEngine.calculate_total(items, self.product_data)
        self.assertEqual(total, 16.61)

    def test_case_3(self):
        """
        Basket: GR1, CF1, SR1, CF1, CF1
        Consolidation: GR1 -> 1, CF1 -> 3, SR1 -> 1
        Expected total: 30.57
        """
        items = [
            {"item": "CF1", "quantity": 3},
            {"item": "GR1", "quantity": 1},
            {"item": "SR1", "quantity": 1}
        ]
        total = PricingEngine.calculate_total(items, self.product_data)
        self.assertEqual(total, 30.57)

if __name__ == "__main__":
    unittest.main()
