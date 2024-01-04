import random
# Import the day_014Finalprojectdata to use the data variable
import day_014Finalprojectdata

# Ask if the user want to play higher or lower
play_again = str(input("Do you want to play Higher or Lower: "))
# Set win and score == True and 0
win = True
score = 0


# Create some function
def print_what(index_of_country):
    # Return 3 thing(the name, the description and the country)
    return (f"{day_014Finalprojectdata.data[index_of_country]['name']}, "
            f"{day_014Finalprojectdata.data[index_of_country]['description']}, "
            f"{day_014Finalprojectdata.data[index_of_country]['country']}")


# If the user lose once or don't want to play it will stop
while play_again == "y" or win:
    # Create variable
    win = True
    # Take a random 2 team out of 50 team and it maybe a little chance to have the same team
    team_A = random.randint(0, 4)
    team_B = random.randint(0, 49)
    # Save the follower of both team
    team_A_follower = day_014Finalprojectdata.data[team_A]['follower_count']
    team_B_follower = day_014Finalprojectdata.data[team_B]['follower_count']
    # Print the score
    print(f"Your current score is : {score}")
    # Print team A
    print(f"Compare A: {print_what(team_A)}")
    print("""     _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)
    """)
    # Print team B
    print(f"Against B: {print_what(team_B)}")
    # Check what team will win
    # If they team A did not win, so it team B
    who_will_win = "B"
    if team_A_follower > team_B_follower:
        who_will_win = "A"
    # Ask the user who has more follower?
    guess_who_win = str(input("Who has more follower ? A or B: ")).upper()
    # Check if the user was right?
    if guess_who_win == who_will_win:
        print(f"You are right! team {guess_who_win} has more follower")
        # Give the user 1 score
        score += 1
    else:
        # Set both win and play_again to False and n because if it just 1 in 2 have the old variable it will run again!
        print(f"Sorry, that's wrong. Final score: {score}")
        win = False
        play_again = "n"
    print()
