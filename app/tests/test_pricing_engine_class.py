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

    def agreggated_match_total(self):
        """
        Test if the sum of the output aggregated items matches the total
        """
        items = [
            {"item": "CF1", "quantity": 3},
            {"item": "GR1", "quantity": 1},
            {"item": "SR1", "quantity": 1}
        ]
        aggregated = []
        for entry in items:
            code = entry["item"]
            qty = entry["quantity"]
            aggregated[code] = aggregated.get(code, 0) + qty
        total = PricingEngine.calculate_total(items, self.product_data)['final_total']
        self.assertEqual(total, sum(aggregated))

    def test_undiscounted_price(self):
        """
        Test scenario with no discounts triggered (e.g., each product below threshold).
        Just confirms the original and final totals match exactly, 
        and breakdown has no per-product discount.
        
        Basket:
          GR1 -> 1, SR1 -> 2, CF1 -> 2
          None of these hits the discount threshold, so final = original.
        """
        items = [
            {"item": "GR1", "quantity": 1},
            {"item": "SR1", "quantity": 2},
            {"item": "CF1", "quantity": 2}
        ]
        # listed price = GR1(3.11) + SR1(2*5.00=10.00) + CF1(2*11.23=22.46) => 35.57
        result = PricingEngine.calculate_total(items, self.product_data)

        self.assertEqual(len(result["breakdown"]), 3)
        self.assertAlmostEqual(result["original_total"], 35.57, places=2)
        self.assertAlmostEqual(result["final_total"], 35.57, places=2)

        for prod in result["breakdown"]:
            self.assertAlmostEqual(prod["original_price"], prod["discounted_price"], places=2)

    def test_breakdown_correctness(self):
        """
        Verify each breakdown entry matches expected code, quantity, 
        original and discounted prices for a simple basket.
        
        Basket:
          GR1 -> 2, SR1 -> 1
          GR1 triggers BOGO, SR1 no discount for quantity=1
        """
        items = [
            {"item": "GR1", "quantity": 2},
            {"item": "SR1", "quantity": 1}
        ]
        result = PricingEngine.calculate_total(items, self.product_data)

        self.assertEqual(len(result["breakdown"]), 2)
        self.assertAlmostEqual(result["original_total"], 11.22, places=2)
        self.assertAlmostEqual(result["final_total"], 8.11, places=2)
        self.assertEqual(len(result["breakdown"]), 2)

        # Convert breakdown to a dict by product code
        bd_map = {b["code"]: b for b in result["breakdown"]}
        
        # GR1 checks
        self.assertEqual(bd_map["GR1"]["quantity"], 2)
        self.assertAlmostEqual(bd_map["GR1"]["original_price"], 6.22, places=2)
        self.assertAlmostEqual(bd_map["GR1"]["discounted_price"], 3.11, places=2)
        
        # SR1 checks
        self.assertEqual(bd_map["SR1"]["quantity"], 1)
        self.assertAlmostEqual(bd_map["SR1"]["original_price"], 5.00, places=2)
        self.assertAlmostEqual(bd_map["SR1"]["discounted_price"], 5.00, places=2)

    def test_case_1(self):
        """
        Basket: GR1, GR1
        Consolidation: GR1 -> 2
        Expected total: 3.11
        """
        items = [
            {"item": "GR1", "quantity": 2}
        ]
        total = PricingEngine.calculate_total(items, self.product_data)['final_total']
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
        total = PricingEngine.calculate_total(items, self.product_data)['final_total']
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
        total = PricingEngine.calculate_total(items, self.product_data)['final_total']
        self.assertEqual(total, 30.57)

if __name__ == "__main__":
    unittest.main()
