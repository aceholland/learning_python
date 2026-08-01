<<<<<<< HEAD
#reduce function

from functools import reduce
l=[112, 3948, 12, 13, 48950, 1, 123, 0, 23]

def greater(a,b):
    if a>b:
        return a
    return b

result = reduce(greater,l)

print(result)
=======
i=int(input("enter a number: "))

table=[ i*n for n in range (1,11)]

print(table)

with open("tables.txt", "a") as f:
    f.write(f"table of {i} is {table} \n")
>>>>>>> 9717ecac3e7de8b95e402c145e75a2b25f53dbbc
