class Calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The Square is {self.n * self.n}")

    def cube(self):
        print(f"The Cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The SquareRoot is {self.n ** 0.5}")
    
    @staticmethod
    def hello():
        print("Hello there")

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()
