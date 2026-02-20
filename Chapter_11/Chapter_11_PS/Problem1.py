class twoDVector :
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2D vectors are {self.i}i + {self.j}j")

class threeDVector(twoDVector) :
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The 3D vectors are {self.i}i + {self.j}j + {self.k}k")

a = twoDVector(1,2)
b = threeDVector(2,4,6)

a.show()
b.show()