import pandas as pd


# Function to show instructions
def show_instructions():
    print('''
    ***** Instructions ******

    This is an item comparison tool.
    It asks the user for their budget
    and the amount of items they are comparing.

    For each item, enter:
    - The name of the item
    - The quantity of items
    - The price of the items
    - The weight of the items

    When you have entered all of the items, prices, quantities, and weights,
    press 'xxx' to finish.

    The program will then display the item/s details
    including the cost of each item, the total cost,
    the unit price, and the recommended item based on the unit price.

    **************************
    ''')


# Function to get yes/no response from user
def yes_no(question):
    while True:
        response = input(question).strip().lower()
        if response in ["yes", "y"]:
            show_instructions()
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


# Function to get non-empty string input
def not_blank(question, error):
    while True:
        response = input(question).strip()
        if response != "":
            return response
        else:
            print(error)


# Function to get positive number input
def num_check(question, error, num_type=int):
    while True:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Function to get expenses
def get_expenses(budget):
    expenses = []
    remaining_budget = budget

    while True:
        item_name = not_blank("Item name (enter 'xxx' to finish): ", "Please enter a valid item name.")

        if item_name.lower() == "xxx":
            break

        price = num_check("Price per item: $", "Please enter a valid price.", int)

        # Check if there are sufficient funds
        max_quantity = remaining_budget // price
        quantity = num_check(f"Quantity (max {max_quantity}): ",
                             f"Please enter a valid quantity (max {max_quantity}).", int)

        if quantity * price > remaining_budget:
            print("You have insufficient funds to purchase this quantity.")
            continue

        weight = float(input("Enter weight in grams: "))

        # Convert weight to kg if less than 1000 grams
        if weight < 1000:
            weight_display = f"{weight} g"
        else:
            weight = weight / 1000
            weight_display = f"{weight} kg"

        # Calculate unit price based on weight
        unit_price = price / weight if weight > 0 else 0

        expenses.append({"Item": item_name, "Price": price,
                         "Quantity": quantity, "Weight": weight_display,
                         "Unit Price": unit_price})

        remaining_budget -= quantity * price

    expenses_df = pd.DataFrame(expenses)

    # Determine recommended item based on unit price
    recommended_item = expenses_df.loc[expenses_df['Unit Price'].idxmin()]

    return expenses_df, recommended_item


# Function to calculate total cost
def calculate_total_cost(expenses):
    expenses['Cost'] = expenses['Price'] * expenses['Quantity']
    total_cost = expenses['Cost'].sum()
    return expenses, total_cost


# Main routine
def main():
    print("Welcome to the price comparison tool!")

    if yes_no("Would you like to see the instructions? (yes/no): "):
        pass  # Instructions already shown in yes_no function

    budget = num_check("What is your budget? $", "Please enter a valid budget.", int)

    print("\nPlease enter the costs below:")
    expenses_df, recommended_item = get_expenses(budget)
    expenses_df, total_cost = calculate_total_cost(expenses_df)

    print("\nExpense Details:")
    print(expenses_df.to_string(index=False))

    print("\nTotal Cost: ${:.2f}".format(total_cost))

    # Print recommended item
    print("\nRecommended Item based on Unit Price:")
    print(recommended_item)


# Execute main function
if __name__ == "__main__":
    main()
