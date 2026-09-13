from data_manager import (
    search_product,
    search_shop,
    search_facility
)


def chatbot_response(message):

    message = message.lower()

    # Product questions
    if "pen" in message:
        results = search_product("pen")

        if results:
            shop = results[0]

            return (
                f"You can get a pen at {shop['shop_name']}.\n\n"
                f"Shop No: {shop['shop_no']}\n"
                f"Floor: {shop['floor']}\n"
                f"Location: {shop['location']}"
            )

    # Shop questions
    if "nike" in message:
        results = search_shop("nike")

        if results:
            shop = results[0]

            return (
                f"Nike is located at:\n\n"
                f"Shop No: {shop['shop_no']}\n"
                f"Floor: {shop['floor']}\n"
                f"Location: {shop['location']}"
            )

    # Facility questions
    if "washroom" in message or "toilet" in message:

        results = search_facility("washroom")

        if results:
            place = results[0]

            return (
                f"The washroom is on {place['floor']}.\n\n"
                f"Location: {place['location']}"
            )

    return (
        "Sorry, I couldn't understand your request. "
        "Please ask about a shop, product, or facility."
    )
if __name__ == "__main__":

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = chatbot_response(user_input)

        print("\nBot:", response)