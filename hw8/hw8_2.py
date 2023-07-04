def squares():
    for number in range(100000000):
        if number % 2 == 0:
            yield number ** 2

if __name__ == '__main__':
    even_squares = squares()
    for elements in squares():
        print(elements)
