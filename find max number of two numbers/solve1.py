# Given two numbers, write a Python code to find the Maximum of these two numbers.

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))


def findMax(a, b):
    if (a > b):
        return a
    elif (b > a):
        return b
    else:
        print("I guess, these number are equal")


findMax(num1, num2)
