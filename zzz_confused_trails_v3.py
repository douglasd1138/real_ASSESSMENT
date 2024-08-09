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
    - The price of the item
    - The weight of the item 

    When you have entered all of the items, prices, and weights
    press 'xxx' to finish.

    The program will then display the item/s details
    including the cost of each item, the total cost,
    the unit price in dollars per kilogram, and
    the recommended item based on the unit price.

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
            print("Please enter 'yes' or 'no.'")


# Function to get non-empty string input
def not_blank(question, error):
    while True:
        response = input(question).strip()
        if response != "":
            return response
        else:
            print(error)


# Function to get positive number input
def num_check(question, error, num_type=float):
    while True:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print("Please enter a valid number.")


# Function to get expenses
def get_expenses(initial_budget):
    item_list = []
    remaining_budget = initial_budget

    while True:
        item_name = not_blank("Item name (enter 'xxx' to finish): ", "Please enter a valid item name.")

        if item_name.lower() == "xxx":
            break

        item_price = num_check("Price per item: $", "Please enter a valid price.", float)
        item_weight_g = num_check("Enter weight (in grams): ", "Please enter a valid weight.", float)

        # Convert weight from grams to kilograms
        item_weight_kg = item_weight_g / 1000
        weight_display = f"{item_weight_kg:.2f} kg"

        # Calculate unit price in dollars per kilogram
        unit_price_per_kg = item_price / item_weight_kg

        # Determine if sufficient funds for this item
        funds_status = "Yes" if remaining_budget >= item_price else "No"

        item_list.append({
            "Item": item_name,
            "Price": item_price,
            "Weight": weight_display,
            "Unit Price": f"${unit_price_per_kg:.2f}",
            "Sufficient Funds": funds_status
        })

        remaining_budget -= item_price

    expenses_dataframe = pd.DataFrame(item_list)

    return expenses_dataframe


# Function to calculate total cost
def calculate_total_cost(expenses_dataframe):
    # Calculate the total cost from the 'Price' column
    total_cost_value = expenses_dataframe['Price'].sum()

    # Remove the 'Cost' column if it exists (though it's not used in this example)
    if 'Cost' in expenses_dataframe.columns:
        expenses_dataframe = expenses_dataframe.drop(columns=['Cost'])

    return expenses_dataframe, total_cost_value


# main routine starts here

print("Welcome to the price comparison tool!")

if yes_no("Would you like to see the instructions? (yes/no): "):
    pass  # Instructions already shown in yes_no function

budget = num_check("What is your budget? $", "Please enter a valid budget.", float)

print("\nPlease enter the costs below:")
expenses_df = get_expenses(budget)
expenses_df, total_cost = calculate_total_cost(expenses_df)

print("\nExpense Details:")
print(expenses_df.to_string(index=False))

# Check for insufficient funds after displaying expenses
insufficient_items = expenses_df[expenses_df['Sufficient Funds'] == "No"]
if not insufficient_items.empty:
    print("\nItems with Insufficient Funds:")
    print(insufficient_items[['Item', 'Price']].to_string(index=False))

print("\nTotal Cost: ${:.2f}".format(total_cost))

# Print recommended item based on unit price
recommended_item = expenses_df.loc[expenses_df['Unit Price'].apply(lambda x: float(x.replace('$', ''))).idxmin()]
print("\nRecommended Item based on Unit Price:")
print(recommended_item[['Item', 'Price', 'Unit Price']])
