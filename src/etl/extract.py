import pandas as pd
from src.utils.config import (
    STORES_FILE,
    PRODUCTS_FILE,
    FUEL_PRICES_FILE,
    POS_TRANSACTIONS_FILE,
)

def load_raw_data():
    stores_df = pd.read_csv(STORES_FILE)
    products_df = pd.read_csv(PRODUCTS_FILE)
    fuel_prices_df = pd.read_csv(FUEL_PRICES_FILE)
    pos_transactions_df = pd.read_csv(POS_TRANSACTIONS_FILE)

    return {
        "stores": stores_df,
        "products": products_df,
        "fuel_prices": fuel_prices_df,
        "pos_transactions": pos_transactions_df,
    }