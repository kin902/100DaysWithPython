import random

# Shortest 125 line
# 1 Create all variable
# The list of card can get
deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
final_or_first_user, final_or_first_computer, computer_deck_or_first_card, computer_score_or_not = "", "", "", ""

# 2 Introduce
print("""88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"bend8"'  88 `"8bbdP"Y8  `"bend8"' 88   `Y8a 88 `"8bbdP"Y8  `"bend8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  """)
print()
print("Welcome to BlackJack")
print()


# 3 All function
def deal_a_card():
    card = deck_cards[random.randint(0, len(deck_cards) - 1)]
    return card


def count_score(some_one_card):
    return sum(some_one_card)


def print_state(user_card_input, computer_card_input, final_or_not):
    """input user_card, computer_card, and it's the final state or not then will print the state"""
    # Check if this is the final print or the first print
    global final_or_first_user, final_or_first_computer, computer_deck_or_first_card, computer_score_or_not
    if not final_or_not:
        # Computer first card
        computer_deck_or_first_card = computer_card_input[0]
        # My card
        final_or_first_user = "card"
        # Help to print computer first card
        final_or_first_computer = "first card"
        # Decide to show the computer score or not
        computer_score_or_not = ""
    elif final_or_not:
        final_or_first_computer = "final hand"
        computer_score_or_not = f", with {count_score(computer_card_input)} score!"
        computer_deck_or_first_card = computer_card_input
        final_or_first_user = "final hand"
    # Just printing the state
    print(f"Your {final_or_first_user} : {user_card_input}, current score: {count_score(user_card_input)}")
    print(f"Computer {final_or_first_computer} : {computer_deck_or_first_card}{computer_score_or_not}")


def new_card(some_one_card):
    """Just type y to get another card and n for don't"""
    # Ask do the user want to get another card
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while get_another_card == "y":
        # Add another random card to user deck
        some_one_card.append(deal_a_card())
        # Count the scores
        score = count_score(some_one_card)
        # Print the state
        print_state(some_one_card, computer_card, False)
        # if the score went over 21 if it true you will bust
        if score > 21:
            return some_one_card
        # Ask the user again
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    # Return the user the final deck after adding
    return some_one_card


# 4 code
# Ask do the user want to play blackjack
want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
while want_to_play == "y":
    # Create the variable because by create in here at the end we don't need to reset all state
    user_score = int()
    computer_score = int()
    # The user and computer card
    user_card = list([])
    computer_card = list([])
    # Give our 2 player some random card
    for i in range(0, 2):
        user_card.append(deal_a_card())
        computer_card.append(deal_a_card())
    # Calculate the score
    user_score = count_score(user_card)
    computer_score = count_score(computer_card)
    # Print the state for 2 player
    print_state(user_card, computer_card, False)
    # The user turn
    # This will replace the user old deck by the new one in the function
    user_card = new_card(user_card)
    # The computer turn
    print("The computer is thinking")
    if random.randint(0, 10) > 4:
        print("The computer choose to get another card")
        # Give the computer a random card
        computer_card.append(deal_a_card())
    if sum(user_card) and 11 in user_card:
        user_card.remove(11)
        user_card.append(1)
    # Calculate again the state and print it out
    user_score = count_score(user_card)
    computer_score = count_score(computer_card)
    print_state(user_card, computer_card, True)
    # Few, finally print who win, who lose
    if user_score == computer_score or user_score > 21 and computer_score > 21:
        print("It's a draw")
    elif computer_score > 21:
        print("Opponent went over. You win")
    elif user_score > 21:
        print("Bust")
    elif user_score > computer_score:
        print("You win")
    elif computer_score > user_score:
        print("You lose")
    print()
    # Ask again do the user want to play again
    want_to_play = input("Do you want to play a game of Blackjack again? Type 'y' or 'n':")
