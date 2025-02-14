class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


vikas = Employee()
vikas.language = "JavaScript" # This is an instance attribute
print(vikas.language, vikas.salary)

