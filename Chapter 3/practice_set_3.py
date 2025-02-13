#  Display User Entered Name with "Good Afternoon"

name = input("Enter your name: ")
print("Good Afternoon, " + name + "!")

# or

# print(f"Good Afternoon {name} !")




# Fill in Name and Date in a Letter Template

name = input("Enter your name: ")
date = input("Enter the date: ")

letter = f'''Dear {name},
You are selected!
{date}'''

print(letter)




# Detect Double Spaces in a String

text = input("Enter a sentence: ")
if "  " in text:
    print("Double spaces detected!")
else:
    print("No double spaces found.")




# Replace Double Spaces with Single Space

text = input("Enter a sentence: ")
new_text = text.replace("  ", " ")
print("Updated Text:", new_text)





# Format the Letter Using Escape Sequence Characters

letter = "Dear Vikas,\n\tThis Python Course is nice.\nThanks!"
print(letter)
