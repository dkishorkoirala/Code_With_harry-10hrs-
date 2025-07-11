class Employee:
    def __init__(self):
        print("Consturctor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Consturctor of programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Consturctor of manager")
    c = 3

# o = Employee()
# print(o.a) #prints the a attribute

# o = Programmer()
# print(o.a) #prints the a attribute
# print(o.b) #prints the b attribute


o = Manager()
print(o.a, o.b, o.c)
