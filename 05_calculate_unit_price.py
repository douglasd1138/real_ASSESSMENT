

def calculate_unit_price(cost, units):
    if units == 0:
        return None
    unit_price = cost / units
    return unit_price


# Example usage:
total_cost = 18
num_units = 2
unit_price_result = calculate_unit_price(total_cost, num_units)
if unit_price_result is not None:
    print("Unit price:", unit_price_result)
else:
    print("Number of units cannot be zero.")
