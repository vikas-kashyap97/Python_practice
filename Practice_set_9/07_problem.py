

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("Python" in line):
        print(f"Yes Python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No Python is not present")




    # for checking in every line of the file 


#     with open("log.txt") as f:
#     lines = f.readlines()

# found = False  # Track if at least one occurrence is found

# for lineno, line in enumerate(lines, start=1):
#     if "Python" in line:
#         print(f"Yes, 'Python' is present. Line no: {lineno}")
#         found = True

# if not found:
#     print("No, 'Python' is not present in any line.")
