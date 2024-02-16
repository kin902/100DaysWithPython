"""
Jimmy = turtle.Turtle
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""
import prettytable
# Create an object
table = prettytable.PrettyTable()
# Create first column
table.add_column("Pokemon name", ["Pikachu", "Charmander", "Squirtle"])
# Create the second column
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
table.clear()
print()
