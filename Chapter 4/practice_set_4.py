# 1. Store seven fruits in a list entered by the user


fruits = []
f1 = input("Enter fruit name: ")
fruits.append(f1)

f2 = input("Enter fruit name: ")
fruits.append(f2)

f3 = input("Enter fruit name: ")
fruits.append(f3)

f4 = input("Enter fruit name: ")
fruits.append(f4)

f5 = input("Enter fruit name: ")
fruits.append(f5)

f6 = input("Enter fruit name: ")
fruits.append(f6)

f7 = input("Enter fruit name: ")
fruits.append(f7)

                 # or

# for i in range(7):
#     fruit = input(f"Enter fruit {i+1}: ")
#     fruits.append(fruit)

# print("List of fruits:", fruits)


# 2. Accept marks of 6 students and display them in a sorted manner

marks = []
for i in range(6):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

marks.sort()
print("Sorted marks:", marks)



# 3. Check that a tuple cannot be changed in Python


a = (1, 2, 3, 4)
# a[0] = 10  # This will cause an error
print(a)



# 4. Sum a list with 4 numbers


numbers = [10, 20, 30, 40]
total = sum(numbers)
print("Sum of the list:", total)




# 5. Count the number of zeros in a tuple

a = (7, 0, 8, 0, 0, 9)
zero_count = a.count(0)
print("Number of zeros:", zero_count)
