print("Welcome to tip calculate!")
paid = input("What was the total bill?: $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
number_of_people = input("How many people to split the bill?")
paid = float(paid)
percentage_tip = float(percentage_tip)
number_of_people = int(number_of_people)
percentage_tip = percentage_tip + 100
the_money_to_tip = (paid * percentage_tip) / 100
the_money_of_one_people = the_money_to_tip / number_of_people
the_money_of_one_people = str(round(the_money_of_one_people, 2))
print("Each person should pay: $" + the_money_of_one_people)
