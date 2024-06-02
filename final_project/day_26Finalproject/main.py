import pandas

# TODO 1. Create a dictionary in this format:
nato_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = list(input("Input a word:  "))
word = [character.upper() for character in word]
output = []
for character in word:
    for (index, row) in nato_alphabet.iterrows():
        if character == row.letter:
            output.append(row.code)

print(output)
