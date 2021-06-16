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