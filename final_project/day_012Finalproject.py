import random
# 1. Introduce
print("""                                                       ""                          
                                                                                   
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba, 88 8b,dPPYba,   ,adPPYb,d8  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    "" 88 88P'   `"8a a8"    `Y88  
8b       88 88       88 8PP"""""""        `"Y8ba,   `"Y8ba,  88 88       88 8b       88  
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I 88 88       88 "8a,   ,d88  
 `"bendP"Y8  `"bendP'Y8  `"bend8"' `"bendP"' `"bendP"' 88 88       88  `"bendP"Y8  
 aa,    ,88                                                            aa,    ,88  
  "Y8bbdP"                                                              "Y8bbdP"                                   

        88                      
  ,d    88                      
  88    88                      
MM88MMM 88,dPPYba,   ,adPPYba,  
  88    88P'    "8a a8P_____88  
  88    88       88 8PP"""""""  
  88,   88       88 "8b,   ,aa  
  "Y888 88       88  `"bend8"'             88                                 
                                           88                                 
                                           88                                 
8b,dPPYba,  88       88 88,dPYba,,adPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'   `"8a 88       88 88P'   "88"    "8a 88P'    "8a a8P_____88 88P'   "Y8  
88       88 88       88 88      88      88 88       d8 8PP""""""" 88          
88       88 "8a,   ,a88 88      88      88 88b,   ,a8" "8b,   ,aa 88          
88       88  `"bendP'Y8 88      88      88 8Y"bend8"'   `"bend8"' 88          
                                                                              """)


# 2. Create some function
def one_attempt(the_number_need_to_guess, attempt_left):
    # If the player have 0 guess so the user immediately lose
    while attempt_left > 0:
        # The user to guess one number
        number_guess = int(input("Make a guess: "))
        # Checking if the number is correct or too high or woo low
        if number_guess == the_number_need_to_guess:
            return True
        if number_guess > the_number_need_to_guess:
            print("Too high")
        else:
            print("Too low")
        # Ask the user to guess again
        print("Guess again")
        # Subtract the user attempt to guess
        attempt_left -= 1
        # Print the remaining attempt for the user
        print(f"You have {attempt_left} attempts remaining to guess the number.")
    return False


# 3. Code
play_again = input("Do you want to play Guessing The Number?, type y for yes and n for no: ")
while play_again == "y":
    # Generate a random number between 0, 100
    number_to_guess = random.randint(0, 100)
    # How many attempt can the user guess
    attempt = 10
    # To Ask if the user want to choose the hard or the easy level
    print("I'm thinking of a number between 0 - 100")
    mode = str(input("Choose a difficulty. Type 'easy' or 'hard':")).lower()
    # If the user choose hard so the user only have 5 attempt to guess
    if mode == "hard":
        attempt = 5
    win = one_attempt(number_to_guess, attempt)
    # Check why the func one_attempt return it's the user guess correct the user ran out of attempt
    if win:
        print(f"You got it! The answer was {number_to_guess}.")
    elif not win:
        print("You've run out of guesses, you lose.")
    print()
    # Ask the user if the user want to play again
    play_again = str(input("Do you want to play Guessing The Number again?, type y for yes and n for no")).lower()
