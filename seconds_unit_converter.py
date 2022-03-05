"""
Building a unit converter that converts from any input unit into seconds

To do:
- Validate user input integer is > 0
- Validate user input integer is not exactly 0
- Fix the fact that months is assuming 4 weeks b/c I couldn't solve for floats
- Combine both validations of user starting inputs
- Accept user's input of desired amount and desired starting unit --> convert that to seconds
    - Allow the user to do a multiple-choice select instead of making the user input the starting unit by manually typing it in
    - Or, alternatively, can I make the initial input a seris of query params or just arguments passed?
- Build so that the user can choose their desired output units instead of only handling conversion to seconds
    - Import a dictionary of all of the base units so that I don't have to define each unit conversion as a variable?
"""
import sys

seconds = 1
minutes = 60 * seconds
hours = 60 * minutes
days = 24 * hours
weeks = 7 * days
months = 4 * weeks
years = 365 * days
decades = 10 * years
valid_starting_units = ["decades", "years", "months",
                        "weeks", "days", "hours", "minutes", "seconds"]


# Request user to input their desired amount
user_input_amount = input("Input amount \n")


def validate_user_input_amount():
    if user_input_amount.isdigit():
        global user_input_amount_int
        user_input_amount_int = int(user_input_amount)
        if user_input_amount_int > 0:
            return(user_input_amount_int)
        elif user_input_amount_int == 0:
            sys.exit(print("Invalid input, cannot be 0"))
    else:
        sys.exit(print("Invalid input, must be be integer"))
        


validate_user_input_amount()


# Request user to input their desired starting unit

user_input_starting_unit = input("Input starting unit \n")


def validate_user_input_starting_units():
    if user_input_starting_unit in valid_starting_units:
        return(user_input_starting_unit)
    else:
        sys.exit(print(f"Invalid input, must be be one of {valid_starting_units}"))


validate_user_input_starting_units()


# Define function to convert from user input number and user input units to seconds
## This is obviously really janky and not ooptimal. I bet there's a way to do a lookup or something

def convert_to_answer(user_input_amount_int, user_input_starting_unit):
    if user_input_starting_unit == "seconds":
        return f"{user_input_amount_int} seconds equals {user_input_amount_int * seconds} seconds"
    elif user_input_starting_unit == "minutes":
        return f"{user_input_amount_int} minutes equals {user_input_amount_int * minutes} seconds"
    elif user_input_starting_unit == "hours":
        return f"{user_input_amount_int} hours equals {user_input_amount_int * hours} seconds"
    elif user_input_starting_unit == "days":
        return f"{user_input_amount_int} days equals {user_input_amount_int * days} seconds"
    elif user_input_starting_unit == "weeks":
        return f"{user_input_amount_int} weeks equals {user_input_amount_int * weeks} seconds"
    elif user_input_starting_unit == "months":
        return f"{user_input_amount_int} months equals {user_input_amount_int * months} seconds"
    elif user_input_starting_unit == "years":
        return f"{user_input_amount_int} years equals {user_input_amount_int * years} seconds"
    elif user_input_starting_unit == "decades":
        return f"{user_input_amount_int} decades equals {user_input_amount_int * decades} seconds"
    else:
        sys.exit(print(f"Unkown error"))


answer = convert_to_answer(user_input_amount_int, user_input_starting_unit)
print(answer)
