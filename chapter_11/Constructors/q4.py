class calculator2:
    def __init__(self,n1):
        self.n1=n1

    def square(self):
        print(f"square is {self.n1*self.n1}")

    @staticmethod
    def hello():
        print("hello world")

a=calculator2(56)
a.square()
a.hello()