class Employee:
    a=1

class Programmer(Employee):
    b=2

class Coder(Programmer):
    c=3

o=Employee()
print (o.a)

#print(o.b) # it will give error because a is not inherited by Employee

o=Programmer()
print(o.a)
print(o.b)

o=Coder()
print (o.a)
print (o.b)
print (o.c)