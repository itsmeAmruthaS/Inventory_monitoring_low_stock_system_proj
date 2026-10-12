from pathlib import Path
import pandas as pd


REQUIRED_COLUMNS = {
    "product_id",
    "name",
    "category",
    "quantity",
    "reorder_level",
    "unit_price",
}


def load_inventory(file_path):
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"Inventory file not found: {path}"
        )

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    elif path.suffix.lower() == ".xlsx":
        df = pd.read_excel(path)
    else:
        raise ValueError(
            "Use a CSV or XLSX inventory file."
        )

    # Normalize column names
    df.columns = (
        df.columns.astype(str).str.strip().str.lower()
    )

    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing columns: {sorted(missing)}"
        )

    if df.empty:
        raise ValueError("Inventory file is empty.")

    # Remove accidental whitespace from text fields
    for column in ["product_id", "name", "category"]:
        df[column] = df[column].astype("string").str.strip()

        if df[column].isna().any() or df[column].eq("").any():
            raise ValueError(
                f"{column} cannot contain blank values."
            )

    # Check duplicate product IDs
    if df["product_id"].duplicated().any():
        raise ValueError("Duplicate product IDs detected.")

    # Validate numeric columns
    numeric_columns = [
        "quantity",
        "reorder_level",
        "unit_price",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="raise"
        )

        if df[column].isna().any():
            raise ValueError(
                f"{column} contains missing values."
            )

        if not df[column].map(
            lambda x: float("-inf") < float(x) < float("inf")
        ).all():
            raise ValueError(
                f"{column} must contain finite numbers."
            )

        if (df[column] < 0).any():
            raise ValueError(
                f"{column} cannot contain negative values."
            )

    # Stock quantities must be whole numbers
    for column in ["quantity", "reorder_level"]:
        if not df[column].map(
            lambda x: float(x).is_integer()
        ).all():
            raise ValueError(
                f"{column} must contain whole numbers."
            )

    # Convert validated values to their intended types
    df["quantity"] = df["quantity"].astype(int)
    df["reorder_level"] = df["reorder_level"].astype(int)

    return df