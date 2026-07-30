
#a list contains multiplication table of 7, wap to convert it to a vertical string of numbers

table= [str(7*i) for i in range (1,11)]

s="\n".join(table)
print (s)

#list comprehension to print a list which contains the multiplication table of a user entered number

i=int(input("enter a number: "))

table=[ i*n for n in range (1,11)]

print(table)

