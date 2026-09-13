from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load CSV files once
products = pd.read_csv("data/Product Table.csv")
inventory = pd.read_csv("data/Inventory Table.csv")
shops = pd.read_csv("data/Shop Table.csv")
floors = pd.read_csv("data/Floor Table.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data["message"].lower().strip()


    # --------------------------------
    # FIND PRODUCT
    # --------------------------------

    found_product = None

    for _, product in products.iterrows():

        product_name = str(product["name"]).lower()

        if product_name in user_message:

            found_product = product
            break


    # --------------------------------
    # PRODUCT FOUND
    # --------------------------------

    if found_product is not None:

        product_id = found_product["id"]


        # Find inventory information

        product_inventory = inventory[
            inventory["product_id"] == product_id
        ]


        if not product_inventory.empty:

            inv = product_inventory.iloc[0]

            shop_id = inv["shop_id"]


            # Find shop

            shop = shops[
                shops["id"] == shop_id
            ]


            if not shop.empty:

                shop = shop.iloc[0]

                floor_id = shop["floor_id"]


                # Find floor

                floor = floors[
                    floors["id"] == floor_id
                ]


                if not floor.empty:

                    floor = floor.iloc[0]


                    response = f"""
🛍️ {found_product['name']}

Brand: {found_product['brand']}

Shop: {shop['name']}
Shop No: {shop['shop_number']}

Floor: {floor['floor_name']}

Price: ₹{inv['price']}
Stock Available: {inv['stock']}
"""


                    return jsonify({
                        "response": response
                    })


    # --------------------------------
    # PRODUCT NOT FOUND
    # --------------------------------

    return jsonify({
        "response": "Sorry, I couldn't find that product in the mall."
    })
if __name__ == "__main__":
    app.run(debug=True)