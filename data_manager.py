import pandas as pd
import os


DATA_FOLDER = "data"


def load_data():

    shops_path = os.path.join(DATA_FOLDER, "shops.csv")
    products_path = os.path.join(DATA_FOLDER, "products.csv")
    facilities_path = os.path.join(DATA_FOLDER, "facilities.csv")

    shops = pd.read_csv(shops_path)
    products = pd.read_csv(products_path)
    facilities = pd.read_csv(facilities_path)

    return shops, products, facilities


def search_product(product_name):

    shops, products, facilities = load_data()

    result = products[
        products["product_name"]
        .str.contains(product_name, case=False, na=False)
    ]

    if result.empty:
        return []

    result = result.merge(shops, on="shop_id")

    return result.to_dict("records")


def search_shop(shop_name):

    shops, products, facilities = load_data()

    result = shops[
        shops["shop_name"]
        .str.contains(shop_name, case=False, na=False)
    ]

    return result.to_dict("records")


def search_facility(facility_name):

    shops, products, facilities = load_data()

    result = facilities[
        facilities["facility_name"]
        .str.contains(facility_name, case=False, na=False)
    ]

    return result.to_dict("records")