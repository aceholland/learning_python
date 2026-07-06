from functools import reduce #reduce needs to be imported from functools module 

#Map exmaple 

l=[1,2,3,4,5,6,7,8]
square= lambda x : x*x
sqList= map(square, l)
print(list(sqList))


#Filter example

def even(n):
    if n%2==0:
        return True
    return False

onlyEven= filter(even,l)
print(list(onlyEven))


#Reduce example
def add(a,b):
    return a+b

print(reduce(add, l))#sequential addition

def mul(a,b):
    return a*b

print(reduce(mul, l)) #sequential multiplication

#adds like fibonacci sequence 