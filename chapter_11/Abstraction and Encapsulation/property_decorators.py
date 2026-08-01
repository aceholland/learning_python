class Employee:
    a=1

    @classmethod  #to print the value of a as class atribute that is print 1 and not 45
    def show(cls):
        print(f"the value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname}, {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
e=Employee()
e.a=45


e.name="Anushka Verma"
print(e.fname, e.lname)
e.show()

#This codes use the concept pf Encapsulation and Abstraction as we are hiding the data that is 
# fname and lname and we are using the name property to set the value of fname and lname and 
# we are using the name property to get the value of fname and lname.