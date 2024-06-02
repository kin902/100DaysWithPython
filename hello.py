with open("final_project/day_024Finalproject/Input/Letters/starting_letter.txt") as letter:
    module_letter = str(letter.read())
    module_letter = module_letter.replace("[name]", "hello")
    print(module_letter)
