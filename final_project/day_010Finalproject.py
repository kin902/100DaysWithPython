# 1 Create all variable need
# To check if the user use the old number to continue calculate
next_time = False
next_time_var = int(0)
# A list that contain all number need to calculate
# Here is the index and meaning: 0 - number1, 1 - number2, 2 - answer, 3 - pre answer
math_list = list([0, 0, 0, 0])
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

    # Check if this a new one or a odd one
    # If the odd one we don't need the first number
    if not next_time:
        math_list[0] = float(input("What's your first number? :"))
    elif next_time:
        math_list[3] = math_list[2]
        next_time_var = 3
    print()

    symbol = operator()
    print()

    # Ask the user to insert second number
    math_list[1] = float(input(" What's the next number? :"))

    # Calculate the two number and return to the user
    if symbol == "+":
        math_list[2] = math_list[next_time_var] + math_list[1]
    elif symbol == "-":
        math_list[2] = math_list[next_time_var] - math_list[1]
    elif symbol == "*":
        math_list[2] = math_list[next_time_var] * math_list[1]
    elif symbol == "/":
        math_list[2] = math_list[next_time_var] / math_list[1]

    # After calculate print the final formular
    print(f"{math_list[next_time_var]} {symbol} {math_list[1]} = {math_list[2]}")

    # Check do the user want to continue or end or start a new calculate
    continue_end_start_new = input(f"Type 'y' to continue calculating with {math_list[2]}, or type 'n' to start new "
                                   f"calculation, or type e to end the calculate: ")

    # Check if the user continue to calculate with the old number?
    if continue_end_start_new == "y":
        next_time = True
    # Else then just reset everything to normal
    else:
        next_time = False
        next_time_var = 0
