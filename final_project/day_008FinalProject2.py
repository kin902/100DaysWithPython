alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'à', 'á', 'ả', 'ã', 'ạ', 'â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ', 'ă', 'ằ', 'ắ', 'ẳ', 'ẵ',
            'ặ',
            'đ',
            'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'ê', 'ề', 'ế', 'ể', 'ễ', 'ệ',
            'ì', 'í', 'ỉ', 'ĩ', 'ị',
            'ò', 'ó', 'ỏ', 'õ', 'ọ', 'ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ',
            'ù', 'ú', 'ủ', 'ũ', 'ụ', 'ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự',
            'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ',
            '.', ',', '?', '!', ':', ';', "'", '"', '(', ')', '[', ']', '{', '}',
            '+', '-', '*', '/', '=', '<', '>', '%', '&', '@', '#', '$', '^', '_',
            '~', '/',
            '⇧', '⇪', '↵', '⌫', '⇥', ' ',
            '←', '→', '↑', '↓'
            ]
go_again = "yes"
while go_again != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = str(input("Type your message:\n")).lower()
        shift = int(input("Type the shift number:\n"))
        original_text = str(text)
        text = list(text)
        if direction == "encode":
            for i in range(0, len(text)):
                text[i] = alphabet.index(text[i]) + shift
                while len(alphabet) - 1 < text[i]:
                    text[i] -= len(alphabet)
                text[i] = alphabet[text[i]]
        elif direction == "decode":
            for i in range(0, len(text)):
                text[i] = alphabet.index(text[i]) - shift
                while int(text[i]) < -1:
                    text[i] += len(alphabet)
                text[i] = alphabet[text[i]]
        after_text = str()
        for i in range(0, len(text)):
            after_text += str(text[i])
        print(f"Here is your original text: {original_text}")
        print(f"Here is your {direction} text: {after_text}")
    elif direction == "setting":
        print("Version")
        print("Symbols")
        print("Exit")
        choice = str(input("What do you want to choose?: ")).lower()
        print()
        if choice == "version":
            print("This is version 1.2.0")
            print("The last time update is 16 Jan 2024")
        elif choice == "symbols":
            print("Here is some symbol that you can use but can type:")
            print(" ~, ⇧, ⇪, ↵,  ⌫, ⇥, ←, →, ↑, ↓")
        elif choice == "exit":
            break
    go_again = str(input("Do you want to use ceaser cipher machine again?: ")).lower()
    print()
