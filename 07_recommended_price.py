import pandas as pd

# Define the data for different items
items = [
    {"Item": "Item A", "Price": 10.50, "Quantity": 1},
    {"Item": "Item B", "Price": 7.50, "Quantity": 2},
    {"Item": "Item C", "Price": 12.00, "Quantity": 3},
    # Add more items here
]

# Create a DataFrame from the data
items_df = pd.DataFrame(items)

# Calculate unit price
items_df['Unit Price'] = items_df['Price'] / items_df['Quantity']

# Find the item with the lowest unit price
cheapest_item = items_df.loc[items_df['Unit Price'].idxmin()]

# Print the comparison table
print("Price Comparison:")
print(items_df)

# Print the cheapest item based on unit price
print("\nBest Unit Price:")
print(cheapest_item)
