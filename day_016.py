import prettytable

pokemon_deck = prettytable.PrettyTable()

Pokédex = {
    "0025": {"Name": "Pikachu", "Type": "Electric"},
    "0906": {"Name": "Sprigatito", "Type": "Grass"},
    "0909": {"Name": "Fuecoco", "Type": "Fire"},
    "0912": {"Name": "Quaxly", "Type": "Water"}
}
all_index = ["0025", "0906", "0909", "0912"]
pokemon_deck.add_column(fieldname="Name", column="Type")
pokemon_deck.add_column("Pika", "Elec")

print(pokemon_deck)
