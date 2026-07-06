<<<<<<< HEAD
#divisible by 5

def divisible(n):
    if n%5==0:
        return True
    return False

l=[1, 495894845, 938940, 92894839, 2245, 83894890, 1234]

a=list(filter(divisible,l))

print (a)
=======
try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))

except ZeroDivisionError as v:
    print("Infinite")
>>>>>>> 9717ecac3e7de8b95e402c145e75a2b25f53dbbc
