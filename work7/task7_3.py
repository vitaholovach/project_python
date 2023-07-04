def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))
print(squares)
