import random
'''
# Exercise 13 -Day004
print("Exercise 13 -Day004")
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
heads_tails = random.randint(0, 1)
if heads_tails == 0:
    print("Tails")
elif heads_tails == 1:
    print("Heads")

# Exercise 14 -Day004
print("-------------------------------------------------------------------------------")
print("Exercise 14 -Day004")
names_string = input("")
names = names_string.split(", ")
# The code above converts the input into an array separating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
num_item = len(names)
index = random.randint(1, num_item)
person_will_buy_the_meal = names[index - 1]
print(f"{person_will_buy_the_meal} is going to buy the meal today!")

# Exercise 15 -Day004
print("-------------------------------------------------------------------------------")
print("Exercise 15 -Day004")

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
num = position [1]
character = 0
character_position = position[0]
if character_position == "A":
    character = 0
if character_position == "B":
    character = 1
if character_position == "C":
    character = 2
num = int(num)
map[num - 1][character] = "X"
print(f"{line1}\n{line2}\n{line3}")
'''

# Final Project -Day004
#print("-------------------------------------------------------------------------------")
player_choose = input("What do you shoose? Type 0 for Rock, 1 for Paper or 2 for Scissoers.")
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
       '''
Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer_choose = random.randint(0, 2)
player_choose = int(player_choose)
if player_choose == 0:
    print(Rock)
if player_choose == 1:
    print(Paper)
if player_choose == 2:
    print(Scissors)
print("Computer chose")
if computer_choose == 0:
    print(Rock)
if computer_choose == 1:
    print(Paper)
if computer_choose == 2:
    print(Scissors)

if computer_choose == player_choose:
    print("It's a draw")
if computer_choose == 0 and player_choose == 2 or computer_choose == 1 and player_choose == 0 or computer_choose == 2 and player_choose == 1:
    print("You lose")
if computer_choose == 0 and player_choose == 1 or computer_choose == 1 and player_choose == 2 or computer_choose == 2 and player_choose == 0:
    print("You Win")

