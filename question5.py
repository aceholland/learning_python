#reduce function

from functools import reduce
l=[112, 3948, 12, 13, 48950, 1, 123, 0, 23]

def greater(a,b):
    if a>b:
        return a
    return b

result = reduce(greater,l)

print(result)