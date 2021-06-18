#args and kwargs

def addTwoNumbers(num1, num2):
    return num1 + num2

def addThreeNumbers(num1, num2, num3):
    return num1 + num2 + num3

def addFourNumbers(num1, num2, num3=0, num4=0):
    return num1 + num2 + num3 + num4

# * means dynamic number of arguments
def addNumbers(*nums):
    result = 0
    for num in nums:
        result = result + num
    return result



# * means dynamic number of arguments
def addNumbersWithDefaultArgs(num1 , *nums):
    try:
        result = 0
        for num in nums:
            result = result + num
        return result + num1
    except Exception:
        return 0


def printApplicationStatus(**kwargs):
    try:
        print("name: "+ kwargs["name"])
        for key in kwargs.keys():
            if key == "age":
                print("age :" + str(kwargs["age"]))
                print("application complete")
            else:
                print("application not complete")
    except Exception as e:
        print("Exception : " + e.args[0])

try:
    print("add two no")
    print(addTwoNumbers(10,12))
    print("add three no")
    print(addThreeNumbers(10,12,14))
    print("add four no")
    print(addFourNumbers(10,12,34))
    print("============using args============")
    print("add two no")
    print(addNumbers(10,12))
    print("add three no")
    print(addNumbers(10,12,14))
    print("add four no")
    print(addNumbers(10,12,34,67))
    print("add five no")
    print(addNumbers(10,12,34,56,"kk"))
    print("add ten no")
    print(addNumbers(10,12,34,56,67,10,12,34,56,67))
    print("add zero no")
    print(addNumbersWithDefaultArgs())
except TypeError:
    print("some type error")
except Exception:
    print("Error")
finally:
    print("executed succesfully")

try:
    print(addNumbersWithDefaultArgs())
except TypeError:
    print("Improper parameter passed")

try:
    print(1/"p")
except ZeroDivisionError:
    print("You cannot divide by zero")
except Exception:
    print("Some internal error")
# **kwargs - key value argument pairs

str = [*"PythonClass"]
print(str)

list =[1,2,3,4,5,6,7]

a,*b,c=list

print(a)
print(b)
print(c)

#kwargs - dictionaries

#dictionaries are key value pairs
application={"name":"prabhat","age":24}
application2={"name":"prabhat"}
printApplicationStatus(**application2)

print(addNumbersWithDefaultArgs(1,3,4))
addNumbers = lambda arg1,*args:sum(args)+arg1
print("lambda output")
print(addNumbers(1,3,4))

addNumbers = (lambda arg1,*args:sum(args)+arg1)(1,2,4)
print("lambda output with parameter passed")
print(addNumbers)

cubeOfNumbers = lambda arg1:arg1*arg1*arg1
print("lambda output")
print(cubeOfNumbers(6))