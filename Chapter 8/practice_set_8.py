# 1. Function to Find the Greatest of Three Numbers


# def greatest_of_three(a, b, c):
#     return max(a, b, c)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# print("Greatest number is:", greatest_of_three(num1, num2, num3))



# 2. Function to Convert Celsius to Fahrenheit


# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# temp_c = float(input("Enter temperature in Celsius: "))
# print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temp_c))



# 3. Prevent print() from Printing a New Line

# print("Hello", end=" ")
# print("World")  


# 4. Recursive Function to Calculate the Sum of First N Natural Numbers

# '''
# sum(1) = 1
# sum(2) = 1 + 2
# sum(3) = 1 + 2 + 3
# sum(4) = 1 + 2 + 3 + 4
# sum(5) = 1 + 2 + 3 + 4 + 5

# sum(n) = 1 + 2 + 3 + 4.... n -1 + n
# sum(n) = sum(n-1) + n
# '''

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(4))

# 5. Function to Print Star Pattern for n = 3



# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)


# pattern(3)



#  6. Function to Convert Inches to Centimeters


# def inches_to_cm(inches):
#     return inches * 2.54

# inches = float(input("Enter value in inches: "))
# print(f"{inches} inches is equal to {inches_to_cm(inches)} cm")




# 7. Function to Remove a Given Word from a List and Strip It


# def rem(l, word):
#     n = [] 
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n


# l = ["Vikas", "Rohan", "Shubham", "an"]

# print(rem(l, "an"))



# 8. Function to Print the Multiplication Table of a Given Number



def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
multiplication_table(num)




