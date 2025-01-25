import unittest
from app.pricing_engine import PricingEngine


class TestPricingEngine(unittest.TestCase):
    def setUp(self):
        """
        Set up product data with product codes, names, and prices.
        """
        self.product_data = {
            "GR1": 3.11,  # Green Tea
            "SR1": 5.00,  # Strawberries
            "CF1": 11.23  # Coffee
        }

    def test_aggregated_match_total(self):
        """
        Ensure the sum of discounted prices in the breakdown matches the final total.
        
        Basket:
          CF1 -> 3 (Coffee discount applies)
          GR1 -> 1 (No BOGO triggered)
          SR1 -> 1 (No bulk discount triggered)
        """
        items = [
            {"code": "CF1", "quantity": 3},
            {"code": "GR1", "quantity": 1},
            {"code": "SR1", "quantity": 1}
        ]
        result = PricingEngine.calculate_total(items, self.product_data)

        # Extract final total
        final_total = result["final_total"]

        # Calculate the sum of breakdown discounted prices
        breakdown_total = sum(entry["discounted_price"] for entry in result["breakdown"])

        self.assertAlmostEqual(final_total, breakdown_total, places=2)

    def test_undiscounted_price(self):
        """
        Test scenario where no discounts are triggered.
        
        Basket:
          GR1 -> 1, SR1 -> 2, CF1 -> 2
          None of these quantities meet the discount thresholds.
        """
        items = [
            {"code": "GR1", "quantity": 1},
            {"code": "SR1", "quantity": 2},
            {"code": "CF1", "quantity": 2}
        ]
        result = PricingEngine.calculate_total(items, self.product_data)

        # Total price calculation without discounts
        expected_original_total = 3.11 + (2 * 5.00) + (2 * 11.23)  # 35.57
        self.assertAlmostEqual(result["original_total"], expected_original_total, places=2)
        self.assertAlmostEqual(result["final_total"], expected_original_total, places=2)

        # Verify that no discounted price differs from original price
        for entry in result["breakdown"]:
            self.assertAlmostEqual(entry["original_price"], entry["discounted_price"], places=2)

    def test_breakdown_correctness(self):
        """
        Verify breakdown correctness for a basket with:
          - GR1 -> 2 (BOGO applies)
          - SR1 -> 1 (No discount)
        """
        items = [
            {"code": "GR1", "quantity": 2},
            {"code": "SR1", "quantity": 1}
        ]
        result = PricingEngine.calculate_total(items, self.product_data)

        self.assertAlmostEqual(result["original_total"], 11.22, places=2)  # 2*3.11 + 1*5.00
        self.assertAlmostEqual(result["final_total"], 8.11, places=2)  # 3.11 (BOGO) + 5.00

        breakdown = {entry["code"]: entry for entry in result["breakdown"]}

        self.assertEqual(breakdown["GR1"]["quantity"], 2)
        self.assertAlmostEqual(breakdown["GR1"]["original_price"], 6.22, places=2)
        self.assertAlmostEqual(breakdown["GR1"]["discounted_price"], 3.11, places=2)

        self.assertEqual(breakdown["SR1"]["quantity"], 1)
        self.assertAlmostEqual(breakdown["SR1"]["original_price"], 5.00, places=2)
        self.assertAlmostEqual(breakdown["SR1"]["discounted_price"], 5.00, places=2)

    def test_case_1(self):
        """
        Test the BOGO discount for Green Tea:
        Basket:
          GR1 -> 2 (Buy 1 Get 1 Free)
        """
        items = [{"code": "GR1", "quantity": 2}]
        result = PricingEngine.calculate_total(items, self.product_data)
        self.assertAlmostEqual(result["final_total"], 3.11, places=2)

    def test_case_2(self):
        """
        Test bulk discount for Strawberries:
        Basket:
          SR1 -> 3 (Bulk discount applies: 4.50 each)
          GR1 -> 1
        """
        items = [
            {"code": "SR1", "quantity": 3},
            {"code": "GR1", "quantity": 1}
        ]
        result = PricingEngine.calculate_total(items, self.product_data)

        # Final price = GR1(3.11) + SR1(3 * 4.50) = 16.61
        self.assertAlmostEqual(result["final_total"], 16.61, places=2)

    def test_case_3(self):
        """
        Test all rules combined:
          - CF1: Coffee discount for quantity >= 3
          - GR1: No BOGO triggered (1 item only)
          - SR1: No bulk discount triggered (1 item only)
        
        Basket:
          GR1 -> 1
          SR1 -> 1
          CF1 -> 3
        """
        items = [
            {"code": "GR1", "quantity": 1},
            {"code": "SR1", "quantity": 1},
            {"code": "CF1", "quantity": 3}
        ]
        result = PricingEngine.calculate_total(items, self.product_data)

        # GR1 = 3.11, SR1 = 5.00, CF1 = 3 * (2/3 * 11.23) ≈ 22.46
        self.assertAlmostEqual(result["final_total"], 30.57, places=2)

        # Verify breakdown
        breakdown = {entry["code"]: entry for entry in result["breakdown"]}
        self.assertAlmostEqual(breakdown["GR1"]["discounted_price"], 3.11, places=2)
        self.assertAlmostEqual(breakdown["SR1"]["discounted_price"], 5.00, places=2)
        self.assertAlmostEqual(breakdown["CF1"]["discounted_price"], 22.46, places=2)


if __name__ == "__main__":
    unittest.main()
