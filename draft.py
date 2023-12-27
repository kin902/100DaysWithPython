# 1. Creating variable

# To check if the user use the old number to continue calculate
second_time = False
# Create a list of all variable about calculating
# Index and meaning: 0 - num1, 1 - num2 , 2 - answer, 3 - pre answer
math_list = [0, 0, 0, 0]
# To check if this time we need to calculate with pre answer
pre_answer_of_num1 = 0
#
continue_end_start_new = str("n")
# 2. Introduction


# 3. Code to make it work
while continue_end_start_new == "y" or continue_end_start_new == "n":
    if continue_end_start_new == "n":
        # Ask the user to insert first number
        math_list[0] = float(input("What's the first number? : "))
    elif continue_end_start_new == "y":
        pre_answer_of_num1 += 3
        math_list[3] = math_list[2]
    print()

    # Ask the user to insert a symbol
    # Check if the user input what symbol like *, /, +, -
    print("+")
    print("-")
    print("*")
    print("/")
    symbol = str(input("Pick an operation: "))
    print()

    # Ask the user to insert second number
    math_list[1] = float(input(" What's the next number? :"))

    # Check what does the user want to calculate
    if symbol == "+":
        math_list[1] = math_list[0 + pre_answer_of_num1] + math_list[1]
    elif symbol == "-":
        math_list[1] = math_list[0 + pre_answer_of_num1] - math_list[1]
    elif symbol == "*":
        math_list[1] = math_list[0 + pre_answer_of_num1] * math_list[1]
    elif symbol == "/":
        math_list[1] = math_list[0 + pre_answer_of_num1] / math_list[1]

    print(f"{math_list[0]} {symbol} {math_list[0]} = {math_list[2]}")

    # Check do the user want to continue or end or start a new calculate
    continue_end_start_new = input(f"Type 'y' to continue calculating with {math_list[2]}, or type 'n' to start new "
                                   f"calculation, or type e to end the calculate: ")
