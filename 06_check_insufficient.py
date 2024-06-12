def check_sufficient_funds(balance, item_price):
    if balance >= item_price:
        print("You have sufficient funds to purchase this item.")
    else:
        print("Insufficient funds. You cannot purchase this item.")


# Example usage:
current_balance = 100  # Replace with the user's actual balance
item_price = 75  # Replace with the price of the item
check_sufficient_funds(current_balance, item_price)
