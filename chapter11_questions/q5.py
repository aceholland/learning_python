#write a class vector which represents vector of n dimensions. Overload + and * 
# which calculates sum and dot product

class Vector:

    def __init__(self, i, j, k):
        self.i=i
        self.j=j
        self.k=k

    def __add__(self, v1):
        return Vector(self.i+v1.i, self.j+v1.j, self.k+v1.k)
    
    def __mul__(self,v2):
        return self.i*v2.i + self.j*v2.j + self.k*v2.k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"



v1=Vector(1,2,3)
v2=Vector(4,5,6)
print(v1+v2)
print(v1*v2)
