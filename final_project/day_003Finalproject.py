print("""88                                                          88                        88                                           
88                                                          88                        88              ,d                           
88                                                          88                        88              88                           
88  ,adPPYba,  8b       d8  ,adPPYba,  ,adPPYba, ,adPPYYba, 88  ,adPPYba, 88       88 88 ,adPPYYba, MM88MMM ,adPPYba,  8b,dPPYba,  
88 a8"     "8a `8b     d8' a8P_____88 a8"     "" ""     `Y8 88 a8"     "" 88       88 88 ""     `Y8   88   a8"     "8a 88P'   "Y8  
88 8b       d8  `8b   d8'  8PP"""""""       8b         ,adPPPPP88 88 8b         88       88 88 ,adPPPPP88   88   8b       d8 88          
88 "8a,   ,a8"   `8b,d8'   "8b,   ,aa "8a,   ,aa 88,    ,88 88 "8a,   ,aa "8a,   ,a88 88 88,    ,88   88,  "8a,   ,a8" 88          
88  `"bendP"'      "8"      `"bend8"'  `"bend8"' `"8bbdP"Y8 88  `"bend8"'  `"bendP'Y8 88 `"8bbdP"Y8   "Y888 `"bendP"'  88      """)
print()
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
if 50 >= Love_Score >= 40:
    print(f"Your score is {Love_Score}, you are alright together.")
if 40 >= Love_Score >= 10 or 90 >= Love_Score >= 50:
    print(f"Your score is {Love_Score}.")
