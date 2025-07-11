class Employee:
    language = "py"         #this is a claass attribute
    salary = 120000


dibash = Employee()
dibash.name = "Dibash"      #this is an instance attribute
print(dibash.name,dibash.language, dibash.salary)

rohan = Employee()
rohan.name= "Rohan roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# here name is instance attribute and salary and language are class attribute as they directly belong to the class 