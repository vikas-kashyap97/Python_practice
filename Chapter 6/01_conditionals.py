# if ellif else ladder

a = int(input("Enter yout age: "))

if(a>=18):
    print("You are an adult")
elif(a == 0):
    print("0 can not be the age of any human being")
elif(a<0):
    print("It is a invalid age")    
else:
    print("You are a child")
    
print("End of the program")
    