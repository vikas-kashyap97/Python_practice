# 1. len() function

name = "Vikas Kashyap"
length = len(name)
print(length)  # Output: 14

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(len(fruits))  # Output: 4

# 2.endswith()

text = "Strawberry"
print(text.endswith("rry"))  # Output: True
print(text.endswith("berry"))  # Output: True
print(text.endswith("Straw"))  # Output: False

# 3.count() Function

sentence = "Python is easy. Python is fun."
count_python = sentence.count("Python")
print(count_python)  # Output: 2

# 4. capitalize() Function

text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello world"


# 5. find() Function

sentence = "Python programming is fun"
position = sentence.find("programming")
print(position)  # Output: 7


# 6. replace() Function

sentence = "I love Python"
new_sentence = sentence.replace("Python", "JavaScript")
print(new_sentence)  # Output: "I love JavaScript"
