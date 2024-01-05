# Password Generator Project
import random


print("""                                                                 888 
                                                                 888 
                                                                 888 
88888b.  8888b. .d8888b .d8888b 888  888  888 .d88b. 888d888 .d88888 
888 "88b    "88b88K     88K     888  888  888d88""88b888P"  d88" 888 
888  888.d888888"Y8888b."Y8888b.888  888  888888  888888    888  888 
888 d88P888  888     X88     X88Y88b 888 d88PY88..88P888    Y88b 888 
88888P" "Y888888 88888P' 88888P' "Y8888888P"  "Y88P" 888     "Y88888 
888                                                                  
888                                                                  
888              """)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print()
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = str()
all_possible_place = list()
total_allow_characters = nr_numbers + nr_symbols + nr_letters
index = int()

for n in range(0, total_allow_characters):
    all_possible_place.append(n)


def interpolate(num, listOf):
    while num > 0:
        index_1 = random.randint(0, len(all_possible_place) - 1)
        if all_possible_place[index_1] == index_1:
            slot = index_1
            index_1 = random.randint(0, len(listOf) - 1)
            all_possible_place[slot] = listOf[index_1]
            num -= 1


interpolate(nr_letters, letters)
interpolate(nr_symbols, symbols)
interpolate(nr_numbers, numbers)

for n in range(0, len(all_possible_place)):
    password += all_possible_place[n]
print(f"Here is your password: {password}")
