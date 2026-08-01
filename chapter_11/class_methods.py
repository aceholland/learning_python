class Employee:
    a=1

    @classmethod  #to print the value of a as class atribute that is print 1 and not 45
    def show(cls):
        print(f"the value of a is {cls.a}")

e=Employee()
e.a=45

e.show()