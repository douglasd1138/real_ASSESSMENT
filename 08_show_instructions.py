# shows instructions
def show_instructions():
    print('''\n
    ***** Instructions ******
    
    this is an item comparison tool 
    it asks the user for their budget
    and the amount of items they are comparing.
    
for each item, enter ...
- the name of the item 
- the quantity of items
- the price of the items
- the weight of the items

when you have entered all of the items, price, quantity and weight.
 press 'xxx' to quit.

the program will then display the item/s details
including the cost of each item, the total cost, 
the unit price and the recommended item based on the unit price.

**************************''')


# checks that user response is not blank
def yes_no(question):
    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            print(show_instructions())
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no.")


# loops to make testing faster...
for item in range(0, 3):
    want_help = yes_no("Do you want to read the instructions? ")
    print("You said '{}'\n".format(want_help))
