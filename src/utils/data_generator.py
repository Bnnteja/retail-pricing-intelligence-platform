import pandas as pd
import random
from datetime import datetime, timedelta

stores = ["store_1", "store_2", "store_3"]
fuel_grades = ["Regular", "Midgrade", "Premium", "Diesel"]

products = [
    ("sku_1", "Coke Can", "drinks", 0.50, 1.50, 2.50),
    ("sku_2", "Chips", "snacks", 0.70, 1.75, 3.00),
    ("sku_3", "Cigarettes", "tobacco", 6.00, 8.00, 11.00),
    ("sku_4", "Motor Oil", "auto_accessories", 8.00, 10.00, 16.00),
    ("sku_5", "Lottery Ticket", "lottery", 1.00, 1.00, 5.00),
    ("sku_6", "Car Wash Soap", "car_care", 4.00, 6.00, 10.00),
    ("sku_7", "Beer Can", "beer_wine", 1.20, 2.50, 5.00),
]

def generate_products_file():
    rows = []
    for sku_id, product_name, category, unit_cost, min_price, max_price in products:
        rows.append([sku_id, product_name, category, unit_cost])

    df = pd.DataFrame(rows, columns=[
        "sku_id", "product_name", "category", "unit_cost"
    ])

    df.to_csv("data/sample_raw/products.csv", index=False)
    print("Generated products data")


def generate_stores_file():
    rows = [
        ["store_1", "Tyler Fuel Stop", "Tyler", "TX"],
        ["store_2", "Dallas Fuel Hub", "Dallas", "TX"],
        ["store_3", "Fort Worth Gas", "Fort Worth", "TX"],
    ]

    df = pd.DataFrame(rows, columns=[
        "store_id", "store_name", "city", "state"
    ])

    df.to_csv("data/sample_raw/stores.csv", index=False)
    print("Generated stores data")


def generate_pos_data(num_records=10000):
    rows = []
    start_date = datetime(2026, 1, 1)

    for i in range(num_records):
        sku_id, product_name, category, unit_cost, min_price, max_price = random.choice(products)

        quantity = random.randint(1, 4)
        unit_price = round(random.uniform(min_price, max_price), 2)

        timestamp = start_date + timedelta(
            days=random.randint(0, 30),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
        )

        total_amount = round(quantity * unit_price, 2)

        rows.append([
            f"tx_{i}",
            random.choice(stores),
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            sku_id,
            quantity,
            unit_price,
            total_amount,
        ])

    df = pd.DataFrame(rows, columns=[
        "transaction_id",
        "store_id",
        "timestamp",
        "sku_id",
        "quantity",
        "unit_price",
        "total_amount",
    ])

    df.to_csv("data/sample_raw/pos_transactions.csv", index=False)
    print("Generated POS transactions data")


def generate_fuel_data(days=30):
    rows = []
    start_date = datetime(2026, 1, 1)

    fuel_price_ranges = {
        "Regular": (2.70, 3.20),
        "Midgrade": (3.00, 3.45),
        "Premium": (3.30, 3.85),
        "Diesel": (3.10, 3.70),
    }

    for d in range(days):
        date = start_date + timedelta(days=d)

        for store in stores:
            for grade in fuel_grades:
                low, high = fuel_price_ranges[grade]

                retail_price = round(random.uniform(low, high), 2)
                supplier_cost = round(retail_price - random.uniform(0.12, 0.30), 2)
                competitor_price = round(retail_price + random.uniform(-0.06, 0.06), 2)
                gallons_sold = random.randint(500, 1800)

                rows.append([
                    date.strftime("%Y-%m-%d"),
                    store,
                    grade,
                    retail_price,
                    supplier_cost,
                    gallons_sold,
                    competitor_price,
                ])

    df = pd.DataFrame(rows, columns=[
        "date",
        "store_id",
        "fuel_grade",
        "retail_price",
        "supplier_cost",
        "gallons_sold",
        "competitor_price",
    ])

    df.to_csv("data/sample_raw/fuel_prices.csv", index=False)
    print("Generated fuel pricing data")


if __name__ == "__main__":
    generate_stores_file()
    generate_products_file()
    generate_pos_data()
    generate_fuel_data()