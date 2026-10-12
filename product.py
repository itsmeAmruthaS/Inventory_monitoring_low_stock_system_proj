from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    name: str
    category: str
    quantity: int
    reorder_level: int
    unit_price: float

    @property
    def inventory_value(self):
        return self.quantity * self.unit_price

    @property
    def stock_status(self):
        if self.quantity == 0:
            return "OUT_OF_STOCK"
        elif self.quantity <= self.reorder_level:
            return "LOW_STOCK"
        return "NORMAL"

    @property
    def reorder_quantity(self):
        return max(0, self.reorder_level - self.quantity)