#input name , marks , phone number and format using format function
name=input("Enter name")
marks=int(input("Enter marks"))
phone=int(input("Enter phone number"))

a= "The name of a student is {}, her marks are {}, her phone number is{}".format(name, marks,phone)
print (a)