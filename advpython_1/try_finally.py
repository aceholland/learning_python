def main():
    try:
      a=int(input("enter a number: "))
      print(a)
      return

    except Exception as e:  #program didnt crash , we are getting output
      print (e)
      return

    finally:
     print("I am inside finally") #shows same output as a written print outside of func, 
     #whereas in funct the difference is visible

    print(" I am not inside finally")

main()