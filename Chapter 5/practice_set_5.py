# 1. Create a dictionary of Hindi words with English translations and allow user lookup
hindi_dict = {
    "paani": "water",
    "aakash": "sky",
    "ped": "tree",
    "suraj": "sun"
}

word = input("Enter a Hindi word to get its English translation: ")
translation = hindi_dict.get(word, "Word not found in dictionary")
print("Translation:", translation)




# 2. Input eight numbers from the user and display unique numbers

unique_numbers = set()

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
num6 = int(input("Enter number 6: "))
num7 = int(input("Enter number 7: "))
num8 = int(input("Enter number 8: "))

unique_numbers.update([num1, num2, num3, num4, num5, num6, num7, num8])

print("Unique numbers:", unique_numbers)


# or


unique_numbers = set()

for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    unique_numbers.add(num)

print("Unique numbers:", unique_numbers)





# 3. Can we have a set with 18(int) and "18"(str) as values?
example_set = {18, "18"}
print("Example set with int and str:", example_set)  # Output: {18, '18'}




# 4. What will be the length of the following set?
S = set()
S.add(20)
S.add(20.0)  # 20 and 20.0 are treated as the same in a set
S.add("20")  # String "20" is a separate value
print("Length of S:", len(S))  # Output: 2





# 5. What is the type of S = {}?
S = {}
print("Type of S:", type(S))  # Output: <class 'dict'>





# 6. What is the type of set()?
empty_set = set()
print("Type of empty_set:", type(empty_set))  # Output: <class 'set'>





# 7. Create an empty dictionary and store favorite languages of 4 friends
fav_languages = {}

fav_languages["Vikas"] = input("Enter Vikas's favorite language: ")
fav_languages["Sachin"] = input("Enter Sachin's favorite language: ")
fav_languages["Rahul"] = input("Enter Rahul's favorite language: ")
fav_languages["Shubham"] = input("Enter Shubham's favorite language: ")

print("Favorite languages dictionary:", fav_languages)




# 8. If two friends have the same favorite language, what will happen?

fav_languages = {
    "Vikas": "Python",
    "Sachin": "Java",
    "Rahul": "Python",  # Same language as Vikas
    "Shubham": "C++"
}

print(fav_languages)


# 9. Can we change the values inside a list contained in a set?

S = {8, 7, 12, "Harry", [1, 2]}  # This will give an error
