# asks user what is their budget
def num_check(num_question, error, num_type):
    while True:

        try:
            response = num_type(input(num_question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks that string response is not blank
def not_blank(var_question, error):
    while True:
        response = input(var_question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))

        return response


# main routine starts here

# get number of product
var_how_many = num_check("what is your budget? $",
                     "The number of items must be a whole "
                     "number more than zero", int)
