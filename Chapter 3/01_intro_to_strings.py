# name = "Vikas"  # or
# name = 'Vikas'  # or
# name = '''Vikas''' 

# nameShort = name [0]   # Output: Vikas

# nameShort = name [0:3]   # This extracts characters from index 0 to 2 (3 is exclusive)

# print(nameShort)         # Output: Vik

# name = "Vikas Kashyap"

# Character index mapping (for reference)
#  V   i   k   a   s       K   a   s   h   y   a   p
#  0   1   2   3   4   5   6   7   8   9  10  11  12
# -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# Extract the last character
# last_char = name[-10:]  
# print(last_char)  # Output: 'as Kashyap'

# Extract the last three characters
# last_three_chars = name[-3:-1]  
# print(last_three_chars)  # Output: 'ya'






# Slicing with a skip value

word = "amazing"

print(word[1: 6: 2]) # Output: "mzn"

print(word[: 7]) # word [0: 7] Output: "amazing"

print(word[0:]) # word [0: 7] Output: "amazing"