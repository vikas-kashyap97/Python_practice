f = open("poem.txt")
content = f.read()
if("jungle" in content):
    print("The word jungle is present in the poem")

else:
    print("The word jungle is not present in the poem")

f.close()