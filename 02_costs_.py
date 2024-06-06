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



