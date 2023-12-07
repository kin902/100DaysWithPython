# Exercise 5 - Day002

print("-------------------------------------------------------------------------------")
print("Exerce 5 - Day002")
two_digit_number = input()#39
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
first_number = two_digit_number[0]
second_number = two_digit_number[1]
print(int(first_number) + int(second_number))

# Exercise 6 - Day002

print("-------------------------------------------------------------------------------")
print("Exerce 6 - Day002")
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)
BMI = int(weight) / (height * height)
BMI = int(BMI)
print(BMI)

# Exercise 7 - Day002
print("-------------------------------------------------------------------------------")
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age = int(age)
week_past = age * 52
week_past = int(week_past)

week_of_life = 52 * 90
week_of_life = int(week_of_life)

week_left = week_of_life - week_past
week_left = str(week_left)
print(f"You have " + week_left + " weeks left.")

# Exercise project - Day002
#       Tip calculator
print("-------------------------------------------------------------------------------")
print("Welcome to tip caculater!")
paid = input("What was the total bill?: $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
number_of_peple = input("How many people to split the bill?")
paid = float(paid)
percentage_tip = float(percentage_tip)
number_of_peple = int(number_of_peple)
percentage_tip = percentage_tip + 100
the_money_to_tip = (paid * percentage_tip) / 100
the_money_of_one_people = the_money_to_tip / number_of_peple
the_money_of_one_people = str(round(the_money_of_one_people, 2))
print("Each person should pay: $" + the_money_of_one_people)