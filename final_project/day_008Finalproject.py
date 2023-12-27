print("""                          _       _               
                                  (_)     | |              
  ___ ___  __ _ ___  __ _ _ __ ___ _ _ __ | |__   ___ _ __ 
 / __/ _ \/ _` / __|/ _` | '__/ __| | '_ \| '_ \ / _ \ '__|
| (_|  __/ (_| \__ \ (_| | | | (__| | |_) | | | |  __/ |   
 \___\___|\__,_|___/\__,_|_|  \___|_| .__/|_| |_|\___|_|   
                                    | |                    
                                    |_|                    """)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
go_again = "yes"


# Process Encode | Decode
def process(msg, shift_to, action=None):
    final = str()
    for _i in range(0, len(msg)):
        if alphabet.count(msg[_i]) > 0:
            # Get index
            index = alphabet.index(msg[_i])

            if action == "encode":
                # Update index after shift
                index += shift_to
            else:
                # Update index after shift
                index -= shift_to

            # Check index out of list alphabet
            if index >= len(alphabet):
                index -= len(alphabet)

            # Check index out of list alphabet
            if index < 0:
                index += len(alphabet)

            msg[_i] = alphabet[index]

    for _e in range(0, len(msg)):
        final += msg[_e]

    return final


while go_again != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = str(input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))
    text = list(text)

    if go_again == "yes":
        final_output = process(text, shift, direction)
        print(f"Here's the encoded result: {final_output}")

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
