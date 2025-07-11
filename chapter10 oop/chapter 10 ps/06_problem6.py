from random import randint
class Train:

    def __init__(slf,trainNo):
        slf.trainNo = trainNo

    def book(ram,  fro, to):
        print(f"Ticket is Booked in train no : {ram.trainNo} from {fro} to {to}")
        
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self,  fro, to):
        print(f"Ticket fair in train no : {self.trainNo} from {fro} to {to} is {randint(1000, 5000)}")

t = Train(1234)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")
