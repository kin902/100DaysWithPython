MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}
# Create a list that contain all possible ingredients in any coffee in the MENU
All_possible_ingredients = ["water", "coffee", "milk"]
# Show the user about the drink and its price
print("Here is the MENU")
print(""" ____________________________________
|               MENU                 |
| espresso   :................ 1.5 $ |
| latte      :................ 2.5 $ |
| cappuccino :................ 3.0 $ |
|____________________________________|""")
# This like a bank will count the machine profit has make
total_profit = 0
# Ask the user want to use the coffee machine
use = input("Do you want to use the coffee machine?")
while use == "y":
    # Ask the user want what drink
    order = str(input("What do you want to order? : "))
    # Check if the user type report because it's the only one who work different from other possible order
    if order == "report":
        # Report will print the state to the user
        print(f"Milk : {resources['milk']} ml")
        print(f"Water : {resources['water']} ml")
        print(f"Coffee : {resources['coffee']} g")
        print(f"Profit has make : {total_profit} $")
    # If the user don't type report so let do the drink
    else:
        # Here is the number of ingredient we need to use
        ingredients_need = 3
        # Except for espresso it only has 2 ingredients
        if order == "espresso":
            ingredients_need = 2
        # It helps the machine to compare between the ingredient need and the ingredient the machine hava
        checking_list = int()
        # Check throw all ingredients need and if the machine has enough that ingredients?
        for o in range(0, ingredients_need):
            if MENU[order]['ingredients'][All_possible_ingredients[o]] <= resources[All_possible_ingredients[o]]:
                checking_list += 1
            # If not so print what ingredient are missing
            else:
                print(f"Sorry we don't have enough {All_possible_ingredients[o]}")
        # Ask the user to input the money in
        if checking_list == ingredients_need:
            # The penny worth 0.01 dollar
            penny = float(input("How much penny do you input? : ")) * 0.01
            # The nickel worth 0.05 dollar
            nickel = float(input("How much nickel do you input? : ")) * 0.05
            # The dime worth 0.10 dollar
            dime = float(input("How much dime do you input? : ")) * 0.10
            # The quarter worth 0.25 dollar
            quarter = float(input("How much quarter do you input? : ")) * 0.25
            # Adding all the coin the user has input
            total_money_input = penny + nickel + dime + quarter
            # Check if the user input enough money
            if total_money_input >= MENU[order]['cost']:
                # If yes then use the ingredients to make the coffee and substrata it in the machine storge
                for i in range(0, ingredients_need):
                    resources[All_possible_ingredients[i]] -= MENU[order]['ingredients'][All_possible_ingredients[i]]
                # Give the user the drink
                print(f"Here is your {order} ☕️️")
                # Give the user the change
                print(f"Here is your change: $ {total_money_input - MENU[order]['cost']}")
                # Add the money to our machine mini bank
                total_profit += MENU[order]['cost']
            else:
                # If the user don't input enough money so print this
                print("Oh no you didn't input enough money")
    print()
    # Ask the user want to use the coffee machine again?
    use = input("Do you want to use the coffee machine again?")
