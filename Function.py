'''
 > A function is a block of reusable code that performs a specific task. 
 > Functions provide a way to modularize code, making it more organized, easier to understand, and reusable.
 > You can define your own functions or use built-in functions provided by Python or third-party libraries.
 > Functions can accept multiple parameters, have default parameter values, return multiple values (as tuples), and more.
 > They provide a powerful way to structure and reuse code in Python.
 '''
Syntax:
def function_name(parameters):
    """docstring"""
    # code block
    return value
'''
> def: Keyword used to define a function.
> function_name: Name of the function.
> parameters: Optional list of parameters (inputs) that the function accepts.
> docstring: Optional documentation string that describes what the function does.
> code block: The actual code that the function executes.
> return: Optional statement that specifies the value the function returns.
'''
Program:

def square(x):
    """Return the square of a number."""
    return x ** 2

# Using the function
result = square(5)
print(result)  # Output: 25







