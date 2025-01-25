class PricingEngine:
    @staticmethod
    def calculate_total(items, product_data):
        """
        Calculate the total price for a given list of items and product data.

        Phase 1: Apply single-product rules (BOGO, bulk discount, etc.)
        Phase 2: Apply cross-product (combo) rules if needed.

        :param items: A list of {"item": <product_code>, "quantity": <int>} dicts.
                  e.g. [ {"item": "GR1", "quantity": 2}, {"item": "CF1", "quantity": 1} ]
        :param product_data: A dict mapping product_code -> base_price (float).
                  e.g. { "GR1": 3.11, "SR1": 5.00, "CF1": 11.23 }
        :return: A dict containing the original total, final total after discounts, 
             and a breakdown of prices per product.
        """

        # Aggregate items. In most situations, we'll have a single entry per product.
        aggregated = {}
        for entry in items:
            code = entry["item"]
            qty = entry["quantity"]
            aggregated[code] = aggregated.get(code, 0) + qty

        # Phase 1: Compute base and per-product discounts
        discounted_costs = {}
        original_costs = {}
        for code, qty in aggregated.items():
            base_price = product_data.get(code, 0.0)
            original_cost = qty * base_price

            if code == "GR1":
                # Buy one, get one free
                payable_qty = (qty // 2) + (qty % 2)
                discounted_costs[code] = payable_qty * base_price

            elif code == "SR1":
                # Bulk discount for 3+ strawberries => 4.50 each
                if qty >= 3:
                    discounted_costs[code] = qty * 4.50
                else:
                    discounted_costs[code] = original_cost

            elif code == "CF1":
                # 3+ coffees => each coffee is 2/3 of original price
                if qty >= 3:
                    discounted_costs[code] = qty * (base_price * (2 / 3))
                else:
                    discounted_costs[code] = original_cost

            else:
                discounted_costs[code] = original_cost

            original_costs[code] = original_cost

        # 3) PHASE 2: Combo or Cross-Product Discounts
        #    Example structure: If we had a rule like
        #    "If GR1 and SR1 are both in the cart, apply an extra 1€ discount"
        #    it can go here. We adjust partial_costs after detecting combos.

        # For now, we do nothing here. But the structure is ready for cross-product logic.

        # 4) Summaries
        original_total = sum(original_costs.values())
        final_total = sum(discounted_costs.values())

        # breakdown per product for UI enriching
        breakdown = []
        for code in aggregated:
            breakdown.append({
                "code": code,
                "quantity": aggregated[code],
                "original_price": round(original_costs[code], 2),
                "discounted_price": round(discounted_costs[code], 2)
            })

        return {
            "original_total": round(original_total, 2),
            "final_total": round(final_total, 2),
            "breakdown": breakdown
        }