class Employee:
    language = "python"         #this is a claass attribute
    salary = 120000


    def getInfo(self):
        print(f"The laguage is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

dibash = Employee()
# dibash.language = "JavaScript"      #this is an instance attribute
print(dibash.language, dibash.salary)
dibash.greet()
dibash.getInfo()
# Employee.getInfo(dibash)