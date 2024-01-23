from day_017Data import question_data
play_again = input("Do you want to play True or False?: ")
while play_again == "yes":
    losing = False
    point = 0
    while not losing and point < 13:
        print()
        print(f"Your current point is: {point}")
        print(f"Question number {point}: {question_data[point]['text']} ?")
        user_answer = input("Is it True or False?: ").lower()
        if user_answer == question_data[point]['answer'].lower() == user_answer:
            point += 1
        else:
            print()
            print("OH, you just lose that question")
            losing = True
    play_again = input("Do you want to play True or False again?: ")
