class calculator:
    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2

    def square(self):
        print(f"square of {self.n1} is {self.n1*self.n1} ")
        print(f"square of {self.n2} is {self.n2*self.n2}")

value=calculator(4,5)
value.square()
