class Programmer:
    def __init__(self, name, salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Promit", 2000, 1234)
print(p.name, p.salary, p.pin)
r=Programmer("Rohit", 3000, 2356)
print(r.name, r.salary, r.pin)