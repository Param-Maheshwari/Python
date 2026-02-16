from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book(param, fro, to):
        print(f"Ticket is booked from {fro} to {to} for train no. {param.trainNo}")
    
    def getStatus(self):
        print(f"Train no. {self.trainNo} is running on time")
    
    def getFare(self, fro, to):
        print(f"Fare for train no. {self.trainNo} running from {fro} to {to} is : {randint(500, 2000)}")

t = Train(12463)
t.book("Kota", "Chennai")
t.getStatus()
t.getFare("Kota", "Chennai")

# Nothing happens if i change "self" to "slf" or "param" but its not a good practice reduces readibility.
