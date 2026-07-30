class Employee:
    company="ITC"
    def show(self):
        print(f"Name of employee is {self.name} and company is {self.company}")

'''class Programmer:
      company="ITC"
      def show(self):
        print(f"Name of employee is {self.name} and company is {self.company}")


      def showlanguage(self):
        print(f"the name is {self.name} and he is comfortable with {self.language} language")

'''

class Programmer(Employee):
    company="Microsoft"
    def showlanguage(self):
        print(f"the name is {self.name} and he is comfortable with {self.language} language")

a=Employee()
b=Programmer()

print(a.company, b.company)