#create a class 2D vector and use it to create another class for 3D vector

class twoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")

class threeDVector(twoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

v1 = twoDVector(2, 3)
v2 = threeDVector(4, 5, 6)

v1.show()
v2.show()