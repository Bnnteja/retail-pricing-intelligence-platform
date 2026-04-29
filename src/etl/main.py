from src.etl.extract import load_raw_data
from src.etl.transform import (
    prepare_processed_transactions,
    build_category_sales_summary,
    build_fuel_margin_analysis,
    build_pricing_recommendations,
)
from src.etl.load import save_dataframe
from src.utils.config import (
    PROCESSED_TRANSACTIONS_FILE,
    CATEGORY_SALES_FILE,
    FUEL_MARGIN_FILE,
    PRICING_RECOMMENDATION_FILE,
)

def run_etl():
    raw_data = load_raw_data()

    stores_df = raw_data["stores"]
    products_df = raw_data["products"]
    fuel_prices_df = raw_data["fuel_prices"]
    pos_transactions_df = raw_data["pos_transactions"]

    processed_transactions_df = prepare_processed_transactions(
        pos_transactions_df=pos_transactions_df,
        products_df=products_df,
        stores_df=stores_df,
    )

    category_sales_summary_df = build_category_sales_summary(processed_transactions_df)
    fuel_margin_df = build_fuel_margin_analysis(fuel_prices_df)
    pricing_recommendations_df = build_pricing_recommendations(fuel_margin_df)

    save_dataframe(processed_transactions_df, PROCESSED_TRANSACTIONS_FILE)
    save_dataframe(category_sales_summary_df, CATEGORY_SALES_FILE)
    save_dataframe(fuel_margin_df, FUEL_MARGIN_FILE)
    save_dataframe(pricing_recommendations_df, PRICING_RECOMMENDATION_FILE)

    print("ETL pipeline completed successfully.")
    print(f"Processed transactions saved to: {PROCESSED_TRANSACTIONS_FILE}")
    print(f"Category sales summary saved to: {CATEGORY_SALES_FILE}")
    print(f"Fuel margin analysis saved to: {FUEL_MARGIN_FILE}")
    print(f"Pricing recommendations saved to: {PRICING_RECOMMENDATION_FILE}")

if __name__ == "__main__":
    run_etl()