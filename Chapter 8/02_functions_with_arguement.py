def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"

a = goodDay("Vikas", "Thank you") 
print(a)




# default parameter 

def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Vikas", "Thanks")
goodDay("Rohan")

