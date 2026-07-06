#divisible by 5

def divisible(n):
    if n%5==0:
        return True
    return False

l=[1, 495894845, 938940, 92894839, 2245, 83894890, 1234]

a=list(filter(divisible,l))

print (a)