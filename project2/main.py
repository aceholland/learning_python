import random
n=random.randint(1,100)
a=-1
guesses=1
while (a!=n):
    
    a=int(input("enter your guess: "))
  
    if (a>n):
        print("enter lower number please")
    elif (a<n):
        print("enter higher number please")

    guesses+=1

print(f"you guessed the number {n} in {guesses} guesses")