from final_project.day_016FinalProject import day_016Menu
from final_project.day_016FinalProject import day_016Moneymachine
from final_project.day_016FinalProject import day_016Coffeemaker

print(""" ____________________________________
|               MENU                 |
| espresso   :................ 1.5 $ |
| latte      :................ 2.5 $ |
| cappuccino :................ 3.0 $ |
|____________________________________|""")

money_machine = day_016Moneymachine.MoneyMachine()
coffee_maker = day_016Coffeemaker.CoffeeMaker()
menu = day_016Menu.Menu()

run_again = True
while run_again:

    option = day_016Menu.Menu().get_items()

    order = str(input("WHat do you want to call?: "))

    if order == "report":

        money_machine.report()
        coffee_maker.report()

    elif order == "off":

        run_again = False

    else:

        drink = menu.find_drink(order)

        if coffee_maker.is_resource_sufficient(
                drink) and money_machine.make_payment(drink.cost):

            coffee_maker.make_coffee(drink)
