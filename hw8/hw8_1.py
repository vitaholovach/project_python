def function_name(function):
    def wrapper(*args):
        print("Function operation:", function.__name__)
        return function(*args)
    return wrapper

@function_name
def summation(x, y):
    result = x + y
    return result

@function_name
def multiplication(x, y):
    result = x * y
    return result

print(summation(7, 2))
print(multiplication(8, 3))
