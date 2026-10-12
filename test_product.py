from product import Product

laptop = Product(
    "P101",
    "Laptop",
    "Electronics",
    8,
    10,
    45000
)

print("Product:", laptop.name)
print("Inventory Value:", laptop.inventory_value)
print("Stock Status:", laptop.stock_status)
print("Reorder Quantity:", laptop.reorder_quantity)