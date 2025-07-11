class Employee:
    
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) #prints the a attribute
# print(o.b) #shows an error as there is no b attribute in employww class

o = Programmer()
print(o.a) #prints the a attribute
print(o.b) #prints the b attribute


o = Manager()
print(o.a, o.b, o.c)
