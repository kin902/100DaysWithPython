"""
Jimmy = turtle.Turtle
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""
import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
