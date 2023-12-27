import random

# Project Hangman

# 1. Create the variable
# ======= Declare all variable ======
# Index for generate the random number
list_of_random_word = list(["apple", "banana", "cherry", "orange", "watermelon", "pineapple"])
index = random.randint(0, len(list_of_random_word) - 1)
# Try to get a random word in list
the_random_word = list_of_random_word[index]

# Other stuff with the player code (Represent: Head, Body, Left hand, Right hand, Left feet, Right feet)
how_many_live_left = 6
# Number characters need to guess
how_many_characters_to_guest = len(the_random_word)
# Keep all guessed word
all_the_word_had_guest = list([])
# Keep all player word that guess right
the_word_need_to_guess = list([])
# A slot for input some random index, and it types, vari will change by the time
slot = ""
for n in range(0, len(the_random_word)):
    the_word_need_to_guess += "_"

# 2. The introduce to player
print("""
 _                                             
| |                                            
| |___   ___ _   _ __    __ _   _ __ ____    __ _  _ ___ 
| '_  | /_    | |  _ |  | _  | |  _   _  |  / _ |  |  _ | 
| | | | | (_| | | | | | |(_| | | | | | | | |(_| | | | | |
|_| |_| |_ _,_| |_| |_| |__, | |_| |_| |_| |__,_| |_| |_|
                         __/ |                      
                        |___/                    
""")
print("Welcome to hangman!")
print()

print("Your word is " + str(len(the_random_word)) + " characters long!")
print("_ " * len(the_random_word))

# 3. Creating the code about hangman

# if you guest all correct, or you guest wrong 6 times it will stop the while
while how_many_live_left > 0 or how_many_characters_to_guest == 0:
    print()
    # Get input from player
    the_player_guest = input("Please type your guess: ").lower()

    # Count existed word in guessed list
    guessed_word_count = the_random_word.count(the_player_guest)

    # Player lost one live if guessed:
    # - An existed character which they guested before (First condition)
    # - Or wrong character (Second condition)
    if all_the_word_had_guest.count(the_player_guest) >= 1 or guessed_word_count < 1:
        # Player lost a live
        how_many_live_left -= 1
        # Append the guessed word to list
        all_the_word_had_guest.append(the_player_guest)

    elif guessed_word_count >= 1:
        # Subtract multi-time the guessed character
        how_many_characters_to_guest -= guessed_word_count
        for n in range(0, len(the_word_need_to_guess)):
            if the_random_word[n] == the_player_guest:
                the_word_need_to_guess[n] = the_player_guest
        # Check if player guessed all characters (Win the game)
        if how_many_characters_to_guest == 0:
            break

    # Player try to guess more
    print(f"You have {how_many_live_left} live left!")
    print(f"This is all the word that you guest wrong is: {all_the_word_had_guest} !")
    slot = ""
    slot = str(slot)
    for n in range(0, len(the_random_word)):
        slot += the_word_need_to_guess[n]
    print(f"Word you need to guest left : {slot} !")

# 4.The final result
print()
if how_many_live_left == 0:
    print("OH! Sorry that you lose")
else:
    print("Congratulation !")
print(f"The word is {the_random_word}")
