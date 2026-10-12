from file_handler import load_inventory

df = load_inventory("inventory.csv")

print("File loaded successfully!")
print("Number of products:", len(df))

print("\nInventory data:")
print(df.to_string(index=False))