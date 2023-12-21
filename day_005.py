"""
#Exercise 16_day005
print("Exercise 16_day005")
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_student = int(len(student_heights))
average_height = 0
total_heights = 0
for i in range(0, total_student):
    total_heights += student_heights[i]
int(total_heights)
int(total_student)
average_height = total_heights / total_student
average_height = int(round(average_height))
print(f"total height = {total_heights}")
print(f"number of students = {total_student}")
print(f"average height = {average_height}")

#Exercise 17_Day005
print()
print("-------------------------------------------------------------------------------")
print("Exercise 17_day005")
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for n in range(0, len(student_scores)):
    if highest_score < student_scores[n]:
        highest_score = student_scores[n]
print(f'The highest score in the class is: {highest_score}')

#Exercise 18_day005
print()
print("-------------------------------------------------------------------------------")
print("Exercise 18_day005")
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
for n in range(0, target + 1, 2):
    total += n
print(total)

#Exercise 19_day005
print()
print("-------------------------------------------------------------------------------")
print("Exercise 19_day005")
# Write your code here 👇
for n in range(1, 100 + 1):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)
"""
# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

slot = int()
password = str()
all_possible_place = list()
total_allow_characters = nr_numbers + nr_symbols + nr_letters
index = int()

for n in range(0, total_allow_characters):
    all_possible_place.append(n)

while nr_letters > 0:
    index = random.randint(0, len(all_possible_place) - 1)
    if all_possible_place[index] == index:
        slot = index
        index = random.randint(0, len(letters) - 1)
        all_possible_place[slot] = letters[index]
        nr_letters -= 1

while nr_symbols > 0:
    index = random.randint(0, len(all_possible_place) - 1)
    if all_possible_place[index] == index:
        slot = index
        index = random.randint(0, len(symbols) - 1)
        all_possible_place[slot] = symbols[index]
        nr_symbols -= 1

while nr_numbers > 0:
    index = random.randint(0, len(all_possible_place) - 1)
    if all_possible_place[index] == index:
        slot = index
        index = random.randint(0, len(numbers) - 1)
        all_possible_place[slot] = numbers[index]
        nr_numbers -= 1

for n in range(0, len(all_possible_place)):
    password += all_possible_place[n]
print(f"Here is your password: {password}")