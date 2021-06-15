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
    result = 0
    for num in nums:
        result = result + num
    return result + num1

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
print(addNumbers(10,12,34,56,67))
print("add ten no")
print(addNumbers(10,12,34,56,67,10,12,34,56,67))
print("add zero no")
print(addNumbersWithDefaultArgs())

# **kwargs - key value argument pairs