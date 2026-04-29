import os
import pandas as pd

REPORT_PATH = "outputs/reports/data_quality_report.txt"

def check_missing_values(df, dataset_name):
    missing = df.isnull().sum()
    return f"\nMissing values in {dataset_name}:\n{missing}\n"


def check_duplicate_rows(df, dataset_name):
    duplicates = df.duplicated().sum()
    return f"\nDuplicate rows in {dataset_name}: {duplicates}\n"


def check_negative_profit(processed_transactions_df):
    negative_count = (processed_transactions_df["gross_profit"] < 0).sum()
    return f"\nNegative gross profit records: {negative_count}\n"


def check_fuel_margin(fuel_margin_df):
    low_margin_count = (fuel_margin_df["margin_per_gallon"] < 0).sum()
    return f"\nNegative fuel margin records: {low_margin_count}\n"


def run_data_quality_checks():
    processed_transactions = pd.read_csv("data/sample_processed/processed_transactions.csv")
    fuel_margin = pd.read_csv("data/sample_processed/fuel_margin_analysis.csv")
    pricing_recommendations = pd.read_csv("data/sample_processed/pricing_recommendations.csv")

    report = []
    report.append("Retail Pricing Intelligence Platform - Data Quality Report\n")
    report.append("=" * 70)

    report.append(check_missing_values(processed_transactions, "processed_transactions"))
    report.append(check_missing_values(fuel_margin, "fuel_margin_analysis"))
    report.append(check_missing_values(pricing_recommendations, "pricing_recommendations"))

    report.append(check_duplicate_rows(processed_transactions, "processed_transactions"))
    report.append(check_duplicate_rows(fuel_margin, "fuel_margin_analysis"))
    report.append(check_duplicate_rows(pricing_recommendations, "pricing_recommendations"))

    report.append(check_negative_profit(processed_transactions))
    report.append(check_fuel_margin(fuel_margin))

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

    with open(REPORT_PATH, "w") as file:
        file.write("\n".join(report))

    print(f"Data quality report generated: {REPORT_PATH}")


if __name__ == "__main__":
    run_data_quality_checks()
