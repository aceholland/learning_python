try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))

except ZeroDivisionError as v:
    print("Infinite")