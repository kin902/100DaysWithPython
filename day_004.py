import random

# Exerce 13 -Day004
print("Exerce 13 -Day004")
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
heads_tails = random.randint(0, 1)
if heads_tails == 0:
    print("Tails")
elif heads_tails == 1:
    print("Heads")

# Exerce 14 -Day004
print("-------------------------------------------------------------------------------")
print("Exerce 14 -Day004")
names = input()
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
list(names)
num_item = len(names)
num_item = int(num_item)
print(num_item)
random_num = random.randint(1, num_item)
person_how_will_pay = names[random_num]
print(person_how_will_pay)