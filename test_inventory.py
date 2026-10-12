from product import Product
from inventory_manager import InventoryManager


products = [
    Product("P101", "Laptop", "Electronics", 8, 10, 45000),
    Product("P102", "Mouse", "Accessories", 35, 15, 500),
    Product("P103", "Keyboard", "Accessories", 4, 10, 1200),
    Product("P104", "Monitor", "Electronics", 0, 5, 12000),
    Product("P105", "Office Chair", "Furniture", 12, 5, 6000),
]

inventory = InventoryManager(products)

print("Total Products:", inventory.total_products())
print("Total Units:", inventory.total_units())

print(
    "Inventory Value: ₹",
    f"{inventory.total_inventory_value():,.2f}",
    sep=""
)

print(
    "Low Stock Items:",
    [p.name for p in inventory.low_stock_products()]
)

print(
    "Out of Stock Items:",
    [p.name for p in inventory.out_of_stock_products()]
)

print("\nCATEGORY REPORT")

for category, items in inventory.group_by_category().items():
    print(category, ":", [p.name for p in items])