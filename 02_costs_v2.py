import pandas


# checks that string response is not blank
def not_blank(question, error):
    while True:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))

        else:
            return response


# checks that input is either a float or an integer that is more than zero. takes in custom error message
def num_check(question, error, num_type):
    valid = False

    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets the expenses, returns list which has the data frame and subtotal
def get_expenses(var_fixed):
    # set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get first set of components, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank")
        if item_name.lower() == "xxx":
            break

        price = num_check("how much for a single item? $",
                          "The price must be a number <more than 0>",
                          float)

        if var_fixed == "variable":
            quantity = num_check("how many do you intend on buying:",
                                 "the amount must be a whole number more than zero",
                                 int)

        # add item, quantity and price to list
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub-total
    sub_total = expense_frame['Cost'].sum()

    # currency formatting (uses currency function
    add_dollars = ['Price', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    return [expense_frame, sub_total]


# Print expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


# main routine starts here


# get number of products
how_many = num_check("How many items will you be comparing? ",
                     "The number of items must be a whole "
                     "number more than zero", int)

print()
print("Please enter the costs below ...")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]
