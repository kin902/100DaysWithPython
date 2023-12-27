# 1. Create all variable need
import random

# All possible card can pick from the deck
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Contain the user card and the computer card
user_card = []
computer_card = []

# Contain the percent chance that the computer will pick
chance_to_pick = []

# To check if the user want to play again
play_again = True

# Check if the user want to get another card or no
new_card_add = "y"

# To count the total card or the user and the player
total_user_card = 0
total_computer_card = 0

# 2. Introduce
print()
print("""88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  """)
print()
print("Welcome to BlackJack !")
print()

# 3. code

while play_again:

    for i in range(0, 2):
        # Index to pick a random card
        user_card.append(card_deck[random.randint(0, len(card_deck))])
        total_user_card += user_card[i]
        computer_card.append(card_deck[random.randint(0, len(card_deck))])
        total_computer_card += computer_card[i]

    print(f"Your card is: {user_card}")
    print(f"Computer first card: {computer_card[0]}")

    while new_card_add == "y":
        new_card_add = input("Type 'y' to get another card, type 'n' to pass: ")

        if new_card_add == "y":
            user_card.append(card_deck[random.randint(0, len(card_deck))])
            total_user_card = 0

            for i in range(0, len(user_card)):
                total_computer_card += user_card[i]

    chance_to_pick = 21 - total_computer_card