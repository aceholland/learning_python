#list comprehension to print a list which contains the multiplication table of a user entered number

i=int(input("enter a number: "))

table=[ i*n for n in range (1,11)]

print(table)