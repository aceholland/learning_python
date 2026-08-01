#overwrite len method on a vector of problem 5 to display dimension of vector

class LenVector:

    def __init__(self, l):
        self.l=l

    def __len__(self):
        return len(self.l)
    

a=LenVector([1,2,3])
print(len(a))