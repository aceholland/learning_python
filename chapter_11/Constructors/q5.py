from random import radint

class Travel:

    def __init__(self, train):
        self.train=train


    def book(self, to, fro, train):
        print(f"booking from {fro} to {to} by {train}")

    def getStatus(self, train, fro, to):
        print(f"the {train} is running successfully from {fro} to {to}")

    def fare(self, to, fro, train):
        print(f"fare from {fro} to {to} by {train} is {radint(222,555)} ")