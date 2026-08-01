def myFunc():
    print("Hello world")

if __name__=="__main__":
  print("We are directly exceuting this file")
  myFunc()
  print(__name__) #will print the name of the file where this code is being executed
#if we exceute from main2.py then it will print module and if we execute from module.py then it will print __main__