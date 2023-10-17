# Adding two number using lambda function

# As we already know that the def keyword is used to define a normal function in Python.
# Similarly, the lambda keyword is used to define an anonymous function in Python.

def add_numbers(x, y): return x+y


num1 = 10
num2 = 30

result = add_numbers(num1, num2)
print("The sum of {0} and {1} is {2}".format(num1, num2, result))
