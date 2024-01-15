def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                # Shift lowercase letters
                result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result


# Example usage
plaintext = "Hello, World!"
shift_amount = 3
encrypted_text = caesar_cipher(plaintext, shift_amount)

print("Original text:", plaintext)
print("Encrypted text:", encrypted_text)
