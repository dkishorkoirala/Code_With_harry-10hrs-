class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    
p = Programmer("Dibash", 1200000, "1234")
print(p.name, p.salary, p.company, p.pin)

    
r = Programmer("Rohan", 12000000, "1234")
print(r.name, r.salary, r.company, r.pin)

