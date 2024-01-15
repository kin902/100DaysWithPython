# Generate a list of Vietnamese characters

# Define the base Latin alphabet
latin_alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Define the diacritic marks used in Vietnamese
diacritics = ['à', 'á', 'ả', 'ã', 'ạ', 'â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ', 'ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ',
              'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'ê', 'ề', 'ế', 'ể', 'ễ', 'ệ',
              'ì', 'í', 'ỉ', 'ĩ', 'ị',
              'ò', 'ó', 'ỏ', 'õ', 'ọ', 'ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ',
              'ù', 'ú', 'ủ', 'ũ', 'ụ', 'ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự',
              'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ']

# Combine the base alphabet with diacritics to get the full Vietnamese alphabet
vietnamese_alphabet = [char for char in latin_alphabet] + diacritics

# Print the list of Vietnamese characters
print(vietnamese_alphabet)