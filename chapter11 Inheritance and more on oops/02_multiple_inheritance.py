class  Employee:
    company = 'ITC'
    name = "Default name"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

class Coder():
    language = 'python'
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
    
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The company is {self.company} and he is good with {self.language} language")

        
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()