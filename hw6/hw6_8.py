def display_box(width: int, height: int, character):
    for row in range(height):
        if row == 0 or row == height - 1:
            print(character * width)
        else:
            empty = width - 2
            print(character + (" " * empty) + character)
