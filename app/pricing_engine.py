class PricingEngine:
    @staticmethod
    def calculate_total(items, product_data):
        """
        Calculate the total price for a given list of items and product data.

        :param items: A list of {"item": <product_code>, "quantity": <int>} dicts.
                    Example: [ {"item": "GR1", "quantity": 2}, {"item": "CF1", "quantity": 1} ]
        :param product_data: A dictionary mapping product_code -> base_price (float).
                            Example: { "GR1": 3.11, "SR1": 5.00, "CF1": 11.23 }
        :return: A float representing the total price after applying all discount rules.
        """
        pass
