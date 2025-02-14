# 1. Multiplication Table Using for Loop

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")


# 2. Greet Names Starting with 'S'


l1 = ["Harry", "Saham", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print(f"Hello, {name}!")





# 3. Multiplication Table Using while Loop


num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{num} × {i} = {num * i}")
    i += 1




# 4. Check if a Number is Prime


num = int(input("Enter a number: "))


for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
else:
        print(f"{num} is a prime number")



# 5. Sum of First n Natural Numbers Using while Loop



n = int(input("Enter a number: "))
sum_natural = 0
i = 1

while i <= n:
    sum_natural += i
    i += 1

print(f"Sum of first {n} natural numbers is {sum_natural}")



# 6. Factorial of a Number Using for Loop


n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i
print(f"Factorial of {n} is {factorial}")



# 7. Star Pattern (*, ***, *****) for n = 3


n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")




# 8. Star Pattern (*, **, ***) for n = 3


n = int(input("Enter a number: "))

for i in range(1, n+1):
    print("*"* i, end="")
    print("")


# 9. stars in square pattern 


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)  
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*") 


# 10. multiplication table of n in reversed order using a for loop


n = int(input("Enter a number: "))


for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")

