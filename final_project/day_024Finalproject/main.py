# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACE_HOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names:
    list_of_name = names.readlines()
with open("./Input/Letters/starting_letter.txt") as letters_file:
    letter_contents = letters_file.read()
    for name in list_of_name:
        name = name.strip()
        new_letter = letter_contents.replace(PLACE_HOLDER, name)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
