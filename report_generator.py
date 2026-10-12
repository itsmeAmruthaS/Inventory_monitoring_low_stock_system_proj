from pathlib import Path
import pandas as pd


def products_to_dataframe(products):
    return pd.DataFrame([
        {
            "product_id": p.product_id,
            "name": p.name,
            "category": p.category,
            "quantity": p.quantity,
            "reorder_level": p.reorder_level,
            "unit_price": p.unit_price,
            "inventory_value": p.inventory_value,
            "stock_status": p.stock_status,
            "reorder_quantity": p.reorder_quantity,
        }
        for p in products
    ])


def generate_reports(manager):
    Path("reports").mkdir(exist_ok=True)

    df = products_to_dataframe(manager.products)

    # Full inventory report
    df.to_csv(
        "reports/inventory_summary.csv",
        index=False
    )

    # Low-stock and out-of-stock report
    alerts = df[df["stock_status"] != "NORMAL"]

    alerts.to_csv(
        "reports/low_stock_report.csv",
        index=False
    )

    # Category report
    category_report = (
        df.groupby("category")
        .agg(
            product_count=("product_id", "count"),
            total_units=("quantity", "sum"),
            inventory_value=("inventory_value", "sum"),
        )
        .reset_index()
    )

    category_report.to_csv(
        "reports/category_report.csv",
        index=False
    )

    print("All reports generated successfully.")