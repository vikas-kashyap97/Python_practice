#  1. Find the Greatest of Four Numbers

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))

# greatest = max(num1, num2, num3, num4)
# print("The greatest number is:", greatest)





# 2. Check if a Student is Pass or Fail

# sub1 = float(input("Enter marks for Subject 1: "))
# sub2 = float(input("Enter marks for Subject 2: "))
# sub3 = float(input("Enter marks for Subject 3: "))

# total_marks = sub1 + sub2 + sub3
# percentage = (total_marks / 300) * 100

# if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and percentage >= 40:
#     print("Congratulations! You are passed!", percentage,"%")
# else:
#     print("Ohh! I am so sorry , you are failed.", percentage,"%")




# 3. Detect Spam Comments

# comment = input("Enter a comment: ").lower()

# spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# if any(keyword in comment for keyword in spam_keywords):
#     print("This comment is spam")
# else:
#     print("This comment is not spam")


# 4. Check if Username Contains Less Than 10 Characters


# username = input("Enter your username: ")

# if len(username) < 10:
#     print("Username is valid (Less than 10 characters)")
# else:
#     print("Username is too long (10 or more characters)")


# 5. Check if a Name is Present in the List


# name_list = ["Vikas", "Rahul", "Sachin", "Shubham", "Saurav"]
# name = input("Enter a name to check: ")

# if name in name_list:
#     print(f"{name} is present in the list")
# else:
#     print(f"{name} is not present in the list")




# 6: Calculate Student Grade

# marks = float(input("Enter the student's marks: "))

# if 90 <= marks <= 100:
#     grade = "Ex"
# elif 80 <= marks <= 90:
#     grade = "A"
# elif 70 <= marks <= 80:
#     grade = "B"
# elif 60 <= marks <= 70:
#     grade = "C"
# elif 50 <= marks <= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"The student's grade is: {grade}")



# 7: Detect "Vikas" in a Post


post = input("Enter the post: ").lower()  # Convert to lowercase for case-insensitive search

if "vikas" in post:
    print("The post is talking about Vikas.")
else:
    print("The post is NOT talking about Vikas.")
