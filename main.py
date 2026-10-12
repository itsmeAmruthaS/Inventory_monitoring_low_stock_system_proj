import logging

from product import Product
from inventory_manager import InventoryManager
from file_handler import load_inventory
from report_generator import generate_reports
from logger_config import configure_logging


def main():
    configure_logging()

    try:
        # Step 1: Load inventory data
        df = load_inventory("inventory.csv")

        # Step 2: Create product objects
        products = []

        for _, row in df.iterrows():
            quantity = row["quantity"]
            reorder_level = row["reorder_level"]
            unit_price = row["unit_price"]

            # Validate numeric values
            if quantity < 0 or reorder_level < 0:
                raise ValueError(
                    "Quantity and reorder level cannot be negative."
                )

            if unit_price < 0:
                raise ValueError(
                    "Unit price cannot be negative."
                )

            if not float(quantity).is_integer():
                raise ValueError(
                    "Quantity must be a whole number."
                )

            if not float(reorder_level).is_integer():
                raise ValueError(
                    "Reorder level must be a whole number."
                )

            products.append(
                Product(
                    product_id=str(row["product_id"]).strip(),
                    name=str(row["name"]).strip(),
                    category=str(row["category"]).strip(),
                    quantity=int(quantity),
                    reorder_level=int(reorder_level),
                    unit_price=float(unit_price),
                )
            )

        # Step 3: Initialize inventory manager
        inventory = InventoryManager(products)

        # Step 4: Generate reports
        generate_reports(inventory)

        # Step 5: Display summary
        print("\n===== INVENTORY SUMMARY =====")
        print("Total Products:", inventory.total_products())
        print("Total Units:", inventory.total_units())

        print(
            "Total Inventory Value: ₹{:,.2f}".format(
                inventory.total_inventory_value()
            )
        )

        print(
            "Low-Stock Products:",
            len(inventory.low_stock_products())
        )

        print(
            "Out-of-Stock Products:",
            len(inventory.out_of_stock_products())
        )

        # Step 6: Display alerts
        print("\n===== STOCK ALERTS =====")

        for product in inventory.low_stock_products():
            print(
                f"LOW STOCK: {product.name} | "
                f"Quantity: {product.quantity} | "
                f"Reorder: {product.reorder_quantity}"
            )

        for product in inventory.out_of_stock_products():
            print(
                f"OUT OF STOCK: {product.name} | "
                f"Reorder: {product.reorder_quantity}"
            )

        print("\nReports saved in the reports folder.")

        logging.info("Inventory processing completed successfully.")

    except (FileNotFoundError, ValueError, OSError):
        logging.exception("Inventory processing failed.")
        print("Error: Inventory processing failed.")
        print("Check application.log for details.")

    except Exception:
        logging.exception("Unexpected application error.")
        print("Unexpected error. Check application.log.")


if __name__ == "__main__":
    main()