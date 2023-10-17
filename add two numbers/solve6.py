# Python program to add two numbers with recursive function
def add_numbers_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_numbers_recursive(x+1, y-1)


num1 = 1
num2 = 2

result = add_numbers_recursive(num1, num2)

print("The sum of", num1, "and", num2, "is", result)
