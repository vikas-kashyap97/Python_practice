# Taking input as a string (default behavior)
name = input("Enter your name: ")
print("Your name is:", name)
print("Type of name:", type(name))  # Always <class 'str'>
print("\n")

# Taking input as an integer
age = int(input("Enter your age: "))
print("Your age is:", age)
print("Type of age:", type(age))  # <class 'int'>
print("\n")

# Taking input as a float
height = float(input("Enter your height in meters: "))
print("Your height is:", height)
print("Type of height:", type(height))  # <class 'float'>
print("\n")

# Taking input as a boolean (converting '1' to True and '0' to False)
is_student = bool(int(input("Are you a student? (1 for Yes, 0 for No): ")))
print("Are you a student?:", is_student)
print("Type of is_student:", type(is_student))  # <class 'bool'>
print("\n")

# Taking multiple inputs (split method)
num1, num2 = input("Enter two numbers separated by space: ").split()
print("First number:", num1, "Type:", type(num1))  # Still string
print("Second number:", num2, "Type:", type(num2))  # Still string
print("\n")

# Converting multiple inputs to integers
num1, num2 = map(int, input("Enter two numbers separated by space (for addition): ").split())
print("Sum of two numbers:", num1 + num2)
print("\n")

# Taking list input
numbers = list(map(int, input("Enter multiple numbers separated by space: ").split()))
print("List of numbers:", numbers)
print("Type of numbers:", type(numbers))  # <class 'list'>
