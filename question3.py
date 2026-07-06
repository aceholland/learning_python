#a list contains multiplication table of 7, wap to convert it to a vertical string of numbers

table= [str(7*i) for i in range (1,11)]

s="\n".join(table)
print (s)