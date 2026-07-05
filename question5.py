i=int(input("enter a number: "))

table=[ i*n for n in range (1,11)]

print(table)

with open("tables.txt", "a") as f:
    f.write(f"table of {i} is {table} \n")