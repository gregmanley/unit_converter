"""
Building a unit converter that converts from any input unit into seconds

To do:
- Validate user input integer is > 0
- Validate user input integer is not exactly 0
- Fix the fact that months is assuming 4 weeks b/c I couldn't solve for floats
- Combine both validations of user starting inputs
- Accept user's input of desired amount and desired starting unit --> convert that to seconds
    - Allow the user to do a multiple-choice select instead of making the user input the starting unit by manually typing it in
- Build so that the user can choose their desired output units instead of only handling conversion to seconds
    - Import a dictionary of all of the base units so that I don't have to define each unit conversion as a variable?
"""
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
user_input_starting_int = input("Input amount \n")


def validate_user_input_starting_int():
    if int(user_input_starting_int):
        return(user_input_starting_int)
    else:
        print("Invalid input, must be be integer")


validate_user_input_starting_int()


# Request user to input their desired starting unit
user_input_starting_unit = input("Input starting unit \n")


def validate_user_input_starting_units():
    if user_input_starting_unit in valid_starting_units:
        return(user_input_starting_unit)
    else:
        print(f"Invalid input, must be be one of {valid_starting_units}")


validate_user_input_starting_units()

# Define function to convert from number of input days to desired units


def convert_to_answer():
    return f"{user_input_starting_int} {user_input_starting_unit} equals {answer} seconds"

answer = convert_to_answer(user_input_starting_int, user_input_starting_unit)
