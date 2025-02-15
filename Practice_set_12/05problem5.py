n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
with open("Practice_set_12/tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")