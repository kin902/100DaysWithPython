"""
# Exercise 20 day_008
print()
print("-------------------------------------------------------------------------------")
print("Exercise 20_day008")


# Write your code below this line 👇
def round_up(number_need_to_round):
    round_up_number = number_need_to_round - int(number_need_to_round)
    if round_up_number >= 0.1:
        round_up_number = 1
    else:
        round_up_number = 0
    return int(number_need_to_round) + round_up_number


def paint_calc(height, width, cover):
    can = round_up((height * width) / cover)
    print(f"You'll need {can} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercise 21 day_008
print()
print("-------------------------------------------------------------------------------")
print("Exercise 21_day008")


# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
"""

# Final project - ce asar cipher
print()
print("-------------------------------------------------------------------------------")
print("""                          _       _               
                                  (_)     | |              
  ___ ___  __ _ ___  __ _ _ __ ___ _ _ __ | |__   ___ _ __ 
 / __/ _ \/ _` / __|/ _` | '__/ __| | '_ \| '_ \ / _ \ '__|
| (_|  __/ (_| \__ \ (_| | | | (__| | |_) | | | |  __/ |   
 \___\___|\__,_|___/\__,_|_|  \___|_| .__/|_| |_|\___|_|   
                                    | |                    
                                    |_|                    """)
# Welcome to our
# At here you can access to pi number, prime number calculate, and more...
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
go_again = "yes"


# Process Encode | Decode
def process(msg, shift_to, action=None):
    final = str()
    for _i in range(0, len(msg)):
        if alphabet.count(msg[_i]) > 0:
            # Get index
            index = alphabet.index(msg[_i])

            if action == "encode":
                # Update index after shift
                index += shift_to
            else:
                # Update index after shift
                index -= shift_to

            # Check index out of list alphabet
            if index >= len(alphabet):
                index -= len(alphabet)

            # Check index out of list alphabet
            if index < 0:
                index += len(alphabet)

            msg[_i] = alphabet[index]

    for _e in range(0, len(msg)):
        final += msg[_e]

    return final


while go_again != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = str(input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))
    text = list(text)

    if go_again == "yes":
        final_output = process(text, shift, direction)
        print(f"Here's the encoded result: {final_output}")

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
