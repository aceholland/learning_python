a=int(input("enter a number 1: "))
b=int(input("enter a number 2: "))

if b==0:
    raise ZeroDivisionError("Hey our program is not meant to divide by zero")

else:
    print(f"the result of {a}/{b} is {a/b}")