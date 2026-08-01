#write a class complex to represent complex numbers along with overloaded operators +, * 

class Complex:
    def __init__ (self, real, imaginary):
        self.real=real
        self.imaginary=imaginary


    def __add__(self, c1):
        return Complex(self.real+c1.real, self.imaginary+c1.imaginary)
    
    #a+bi * c+di = (ac-bd) + (ad+bc)i
    def __mul__(self, c2):
        return Complex(self.real*c2.real - self.imaginary*c2.imaginary, self.real*c2.imaginary + self.imaginary*c2.real)

    def __str__(self):
        return (f"{self.real} + {self.imaginary}i")
    
c1=Complex(1,2)
c2=Complex(3,4)

print(c1+c2)
print(c1*c2)

