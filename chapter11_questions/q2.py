#create class pets from animal and dog from pet and add method bark to dog

class animal:
    pass

class pet(animal):
    pass

class dog(pet):

    @staticmethod
    def bark():
        print("woof woof")

d=dog()
d.bark()