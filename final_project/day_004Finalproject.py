import random
print("""                                  88                                                                                      88                                             
                                  88                                                                                      ""                                             
                                  88                                                                                                                                     
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8  8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba, ,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba,  
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"   88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8 I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8  
88         8b       d8 8b         8888[     88       d8 ,adPPPPP88 88       d8 8PP"""""""       88         `"Y8ba,   8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,  88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88         aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88          
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a 88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88         `"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88          
                                            88                     88                                                                                                    
                                            88                     88                                                                                                 """)
print()
print("Welcome to Py Rock, Paper, Scissor")
player_choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
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