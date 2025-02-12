# Demonstrating type() function
print("Checking Data Types Using type() Function:\n")

a = 10           # Integer
b = 3.5          # Float
c = "Hello"      # String
d = True         # Boolean
e = None         # NoneType

# Using type() function to check types
print("Type of a (10):", type(a))  # <class 'int'>
print("Type of b (3.5):", type(b))  # <class 'float'>
print("Type of c ('Hello'):", type(c))  # <class 'str'>
print("Type of d (True):", type(d))  # <class 'bool'>
print("Type of e (None):", type(e))  # <class 'NoneType'>

print("\n")

# Demonstrating Typecasting
print("Typecasting Examples:\n")

# Integer to Float
num_int = 5
num_float = float(num_int)
print("Integer to Float:", num_float)  # 5.0

# Float to Integer
num_float = 5.7
num_int = int(num_float)
print("Float to Integer:", num_int)  # 5 (removes decimal part)

# Integer to String
num = 100
num_str = str(num)
print("Integer to String:", num_str, "Type:", type(num_str))  # "100" <class 'str'>

# String to Integer
str_num = "50"
num = int(str_num)
print("String to Integer:", num, "Type:", type(num))  # 50 <class 'int'>

# String to Float
str_float = "25.75"
num = float(str_float)
print("String to Float:", num, "Type:", type(num))  # 25.75 <class 'float'>

# Float to String
num = 18.99
num_str = str(num)
print("Float to String:", num_str, "Type:", type(num_str))  # "18.99" <class 'str'>

# Boolean to Integer
bool_val = True
num = int(bool_val)
print("Boolean to Integer:", num)  # 1 (True -> 1, False -> 0)

# Integer to Boolean
num = 0
bool_val = bool(num)
print("Integer to Boolean (0):", bool_val)  # False

num = 5
bool_val = bool(num)
print("Integer to Boolean (5):", bool_val)  # True
