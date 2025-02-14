class Employee: 
    language = "Py" # This is a class attribute
    salary = 580000


vikas = Employee()
vikas.name = "Vikas" # This is an instance attribute
print(vikas.name, vikas.language, vikas.salary)

alok = Employee()
alok.name = "Alok"
print(alok.name, alok.salary, alok.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class