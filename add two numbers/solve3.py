# Defining add function and returning the result

def sumFunc(a, b):
    return a+b


num1 = int(input("Please enter num1: "))
num2 = int(input("Please enter num2: "))

print(f'The sum of {num1} and {num2} = {sumFunc(num1, num2)}')
