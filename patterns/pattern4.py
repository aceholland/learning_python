<<<<<<< HEAD
rows = 5
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
=======
for i in range(6):
    for j in range(7):
        if ((i == 0 and (j not in [0, 3, 6])) or
            (i == 1) or
            (i == 2) or
            (i == 3 and j not in [0, 6]) or
            (i == 4 and j in [2, 3, 4]) or
            (i == 5 and j == 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
>>>>>>> 6223bcd7d86b3526360d2f9de4c147200f2b54db
    print()