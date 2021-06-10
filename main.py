print("Hello Pycharm")

#we write function with def keyword
def printMessage(arg1):
    if(type(arg1) is str):
        print(str(3.5) + arg1)
    elif (type(arg1) is int):
        print(int(3.5) + arg1)
    elif (type(arg1) is float):
        print(float(3.5) + arg1)

#value of arg1 will be "6.6"
printMessage(str(6.6))
#value of arg1 will be 6
printMessage(int(6.6))
#value of arg1 will be 6.6
printMessage(float(6.6))


#constructors and destructors
a = 33
b = 200
if b > a:
 print("b is greater than a")


