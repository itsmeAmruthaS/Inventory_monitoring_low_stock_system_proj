from collections import defaultdict


class InventoryManager:

    def __init__(self, products):
        self.products = products

    def total_products(self):
        return len(self.products)

    def total_units(self):
        return sum(product.quantity for product in self.products)

    def total_inventory_value(self):
        return sum(
            product.inventory_value
            for product in self.products
        )

    def low_stock_products(self):
        return [
            product for product in self.products
            if product.stock_status == "LOW_STOCK"
        ]

    def out_of_stock_products(self):
        return [
            product for product in self.products
            if product.stock_status == "OUT_OF_STOCK"
        ]

    def group_by_category(self):
        categories = defaultdict(list)

        for product in self.products:
            categories[product.category].append(product)

        return dict(categories)