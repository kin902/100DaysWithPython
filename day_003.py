# Exercise 8 -Day003
print("Exerce 8 -Day003")
#   Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number = float(number)
odd_or_even = number % 2
odd_or_even = int(odd_or_even)
if odd_or_even == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Exercise 9 -Day003
print("-------------------------------------------------------------------------------")
print("Exerce 9 -Day003")
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = weight / (height ** 2)
if BMI >= 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
if BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
if BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
if BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")

# Exercise 10 -Day003
print("-------------------------------------------------------------------------------")
print("Exerce 10 -Day003")
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
divisible_4 = year % 4
divisible_100 = year % 100
divisible_400 = year % 400
if divisible_4 == 0:
    if divisible_100 == 0:
        if divisible_400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

# Exercise 11 -Day003
print("-------------------------------------------------------------------------------")
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
size = str(size)
add_pepperoni = str(add_pepperoni)
extra_cheese = str(extra_cheese)
bill = 0
# For the size of the pizza
if size == "S":
    bill += 15
if size == "M":
    bill += 20
if size == "L":
    bill += 25
# For the extra topic
if size == "S":
    if add_pepperoni == "Y":
        bill += 1
    if add_pepperoni == "N":
        bill += 0
if size == "L" or size == "M":
    if add_pepperoni == "Y":
        bill += 3
    if add_pepperoni == "N":
        bill += 0
# For the extra cheese
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0
print(f"Your final bill is: ${bill}.")

# Exercise 12 -Day003
print("-------------------------------------------------------------------------------")
print("Exercise 12 -Day003")
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
the_lover_name = name1 + name2
lower_name = the_lover_name.lower()
T = lower_name.count("t")
R = lower_name.count("r")
U = lower_name.count("u")
E = lower_name.count("e")
first_digit = T + R + U + E
L = lower_name.count("l")
O = lower_name.count("o")
V = lower_name.count("v")
E = lower_name.count("e")
second_digit = L + O + V + E
first_digit = str(first_digit)
second_digit = str(second_digit)
Love_Score = first_digit + second_digit
Love_Score = int(Love_Score)
if Love_Score <= 10 or Love_Score >= 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
if Love_Score <= 50 and Love_Score >= 40:
    print(f"Your score is {Love_Score}, you are alright together.")
if Love_Score <= 40 and Love_Score >= 10 or Love_Score <= 90 and Love_Score >= 50:
    print(f"Your score is {Love_Score}.")
