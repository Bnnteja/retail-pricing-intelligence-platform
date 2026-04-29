import pandas as pd

def prepare_processed_transactions(pos_transactions_df, products_df, stores_df):
    df = pos_transactions_df.copy()

    df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    format="%Y-%m-%d %H:%M:%S",
    errors="coerce"
)

    df = df.merge(products_df, on="sku_id", how="left")
    df = df.merge(stores_df, on="store_id", how="left")

    df["gross_profit"] = df["total_amount"] - (df["quantity"] * df["unit_cost"])

    return df


def build_category_sales_summary(processed_transactions_df):
    summary = (
        processed_transactions_df.groupby(["store_id", "category"], as_index=False)
        .agg(
            total_sales=("total_amount", "sum"),
            total_gross_profit=("gross_profit", "sum"),
            total_quantity=("quantity", "sum"),
        )
    )

    return summary


def build_fuel_margin_analysis(fuel_prices_df):
    df = fuel_prices_df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df["margin_per_gallon"] = df["retail_price"] - df["supplier_cost"]
    df["total_margin"] = df["margin_per_gallon"] * df["gallons_sold"]
    df["price_gap_vs_competitor"] = df["retail_price"] - df["competitor_price"]

    return df


def build_pricing_recommendations(fuel_margin_df, min_margin_threshold=0.12):
    df = fuel_margin_df.copy()

    def recommend(row):
        if row["competitor_price"] < row["retail_price"] and row["margin_per_gallon"] > min_margin_threshold:
            gap = row["retail_price"] - row["competitor_price"]
            if gap > 0.03:
                return "Reduce by $0.02"
            return "Review price"
        elif row["margin_per_gallon"] < min_margin_threshold:
            return "Do not reduce - margin too low"
        elif row["competitor_price"] > row["retail_price"] and row["margin_per_gallon"] >= min_margin_threshold:
            return "Hold or increase by $0.01"
        else:
            return "Hold"

    df["recommendation"] = df.apply(recommend, axis=1)

    recommendation_df = df[
        [
            "date",
            "store_id",
            "fuel_grade",
            "retail_price",
            "competitor_price",
            "margin_per_gallon",
            "price_gap_vs_competitor",
            "recommendation",
        ]
    ].copy()

    return recommendation_df