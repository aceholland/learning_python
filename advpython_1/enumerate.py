l=[313,2435,3884, 83948, 7, 10, 99]

'''index=0
for item in l:
    print(f"the item at index {index} is {item}")
    index+=1
    '''
 #this can be simplified in 2 lines using enumerate function

for index, item in enumerate(l):
    print(f"the item at index {index} is {item}")