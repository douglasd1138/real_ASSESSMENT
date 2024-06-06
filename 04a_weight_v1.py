# checks that  user has entered yes / no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    while True:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("please enter either yes or no...\n")


def weight(weight_type):
    # Initialise variables and error message
    error = "Please enter a weight\n"

    while True:

        # ask for weight...
        response = input(" What is the weight (eg 5000g or 5kg) ")

        # checks if last character is g
        if response[0] == "g":
            weight_type = "g"
            # Get amount (everything before the g)
            amount = response[1:]

        # check if last character is kg
        elif response[-1] == "kg":
            weight_type = "kg"
            # Get amount (everything before the kg)
            amount = response[:-1]

        else:
            # Set response to amount for now
            weight_type = "unknown"
            amount = response

        try:
            # Check amount is a number ore than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if weight_type == "unknown" and amount >= 1000:
            kilo_type = yes_no("do you mean {:.2f}kg. ie {:.2f} kilograms? , y/n ".format(amount, amount / 1000))

            # set weight type based on user answer above
            if kilo_type == "yes":
                weight_type = "kg"
            else:
                weight_type = "g"

        elif weight_type == "unknown" and amount < 1000:
            grams_type = yes_no("Do you mean {}g? , y/n".format(amount))
            if grams_type == "yes":
                weight_type = "g"
            else:
                weight_type = "kg"

        # return weight to main routine
        if weight_type == "g":
            return amount
        else:
            goal = (amount / 1000)
            return goal


# Main routine starts here

all_costs = 0

# Loop for quick testing...
for item in range(0, 6):
    weight = weight(type)
    print("weight : {:.2f}".format(weight))
    print()
