class Employee:
    name="Default Name"
    company="ITC"
    def show(self):
        print(f"Name of employee is {self.name} and company is {self.company}")

class Coder:
    company="HCL"
    language="Python"
    def showlanguage(self):
        print(f"the name is {self.company} and he is comfortable with {self.language} language")

class Programmer(Employee, Coder):
    company="Microsoft"
    def showlanguage(self):
        print(f"the name is {self.company} and he is comfortable with {self.language} language")

a=Employee()
b=Programmer()

b.show()
b.showlanguage()


print(a.company, b.company)