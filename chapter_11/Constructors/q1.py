class Employee:
    language="Python"
    salary=10000

    def getInfo(self):
        print(f"language is {self.language} and salary is {self.salary}")

harry=Employee()
harry.language="js"
harry.getInfo()