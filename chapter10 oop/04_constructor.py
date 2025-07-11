class Employee:
    language = "python"         #this is a claass attribute
    salary = 120000

    def __init__(self, name, salary, language):     #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creaing an object")


    def getInfo(self):
        print(f"The laguage is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

dibash = Employee("Dibash", 130000, "JavaScript")
# dibash.name = "Dibash"
print(dibash.name, dibash.salary, dibash.language)

# rohan = Employee()