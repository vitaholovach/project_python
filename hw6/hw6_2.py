import math

def square(side):
    perimeter = side * 4
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return (perimeter, area, diagonal)
