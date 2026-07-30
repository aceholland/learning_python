<<<<<<< HEAD
#input name , marks , phone number and format using format function
name=input("Enter name")
marks=int(input("Enter marks"))
phone=int(input("Enter phone number"))

a= "The name of a student is {}, her marks are {}, her phone number is{}".format(name, marks,phone)
print (a)
=======
#wap to print 3rd, 5th and 7th element using enumerate function

l=[1,2,3,4,5,6,7,8,9]

for i, item in enumerate(l):
    if i==2 or i==4 or i==6:
        print (item)
>>>>>>> 9717ecac3e7de8b95e402c145e75a2b25f53dbbc
