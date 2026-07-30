class Employee:
    def __init__(self):
        print("Employee Constructor called")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Programmer Constructor called")
    b=2

class Coder(Programmer):
    def __init__(self):
        super().__init__() #now the parent class that is the {Programmer} constructor will be called too
        print("Coder Constructor called")
    c=3

'''o=Employee()
print (o.a)

#print(o.b) # it will give error because a is not inherited by Employee

o=Programmer()
print(o.a)
print(o.b)
'''

o=Coder()
print (o.a)
print (o.b)
print (o.c)