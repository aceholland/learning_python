a=89

def func():
    a=3
    print(a) #will print local variable 3

func()
print(a)# will print 89 as its globbal variable

b=898

def func2():
    global b
    b=3
    print(b) #will print global variable 3

func2()
print(b)# will print 3 as its global variable