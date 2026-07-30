myList=[1,4,5,6,7,6]

squaredList=[]

'''for item in myList:
    squaredList.append(item**2)
    '''

squaredList=[item**2 for item in myList]

print (squaredList)

