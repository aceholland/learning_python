#using walrus operator

if ( n:= len([1,2,3,4,5,6,]))>3:
    print(f"the length of the list is too long ({n} elements, expected <=3)")