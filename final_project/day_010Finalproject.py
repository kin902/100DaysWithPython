# 1 Create all variable need
# To check if the user use the old number to continue calculate
next_time = False
# A list that contain all number need to calculate
FIRST_NUMBER = "first_number"
SECOND_NUMBER = "second_number"
RESULT_NUMBER = "result_number"
math_dict = {
    FIRST_NUMBER: 0,
    SECOND_NUMBER: 0,
    RESULT_NUMBER: 0,
}
# Symbol that need to calculate
symbol = str()
# To check if the user want to calculate with the pre answer or and or create a new calculate
continue_end_start_new = str("n")
# 2 Introduce
print(""" ____________________
|  _________________  |
| | file.py + Python| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""")

print()
print("Welcome to Py calculater")
print()


def operator():
    _symbol = ""
    _flag = True

    # Ask the user to insert a symbol
    # Check if the user input what symbol like *, /, +, -
    print("Operator +")
    print("Operator -")
    print("Operator *")
    print("Operator /")

    while _flag:
        _symbol = str(input("Pick an operation: "))
        if _symbol in "+-*/":
            _flag = False

    return _symbol


# 3 code need to calculate
while continue_end_start_new == "y" or continue_end_start_new == "n":
    # First number
    if not next_time:
        math_dict[FIRST_NUMBER] = float(input("What's your first number? :"))

    # Operator
    symbol = operator()
    print()

    # Second number
    math_dict[SECOND_NUMBER] = float(input(" What's the next number? :"))

    # Calculate the two number and return to the user
    if symbol == "+":
        math_dict[RESULT_NUMBER] = math_dict[FIRST_NUMBER] + math_dict[SECOND_NUMBER]
    elif symbol == "-":
        math_dict[RESULT_NUMBER] = math_dict[FIRST_NUMBER] - math_dict[SECOND_NUMBER]
    elif symbol == "*":
        math_dict[RESULT_NUMBER] = math_dict[FIRST_NUMBER] * math_dict[SECOND_NUMBER]
    elif symbol == "/":
        math_dict[RESULT_NUMBER] = math_dict[FIRST_NUMBER] / math_dict[SECOND_NUMBER]

    # After calculate print the final formular
    print(f"{math_dict[FIRST_NUMBER]} {symbol} {math_dict[SECOND_NUMBER]} = {math_dict['result_number']}")

    # Check do the user want to continue or end or start a new calculate
    continue_end_start_new = input(f"Type 'y' to continue calculating with {math_dict['result_number']}, or type 'n' "
                                   f"to start new calculation, or type e to end the calculate: ")

    # Check if the user continue to calculate with the old number?
    if continue_end_start_new == "y":
        math_dict[FIRST_NUMBER] = math_dict[RESULT_NUMBER]
        next_time = True
    # Else then just reset everything to normal
    else:
        next_time = False
