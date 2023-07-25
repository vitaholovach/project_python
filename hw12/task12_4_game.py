from random import randint

sheet = []
for x in range(6):
    sheet.append(["O"] * 6)


def print_sheet(sheet):
    for row in sheet:
        print((" ").join(row))


def random_row(sheet):
    return randint(0, len(sheet) - 1)


def col_random(sheet):
    return randint(0, len(sheet[0]) - 1)


print("Let's start the game Sea battle!")
print_sheet(sheet)
ship_row = random_row(sheet)
col_ship = col_random(sheet)

while True:
    for to_turn in range(10):
        print("Move: ", to_turn)
        row_guess = int(input("Row 0-5:"))
        col_guess = int(input("Col 0-5:"))
        if row_guess == row_ship and col_guess == col_ship:
            print("You sank my ship!")
            break
        else:
            if (row_guess < 0 or row_guess > 5) or (col_guess < 0 or col_guess > 5):
                print("Oh, these coordinates are not in our ocean.")
            elif (sheet[row_guess][col_guess] == "X"):
                print("You already mentioned these coordinates.")
            else:
                print("Pass!")
                sheet[row_guess][col_guess] = "X"
        print_sheet(sheet)
        if to_turn == 9:
            print("Game over!")
    game = input('Do you want to play again? If yes - press "Enter", if not - enter "no"')
    if game == 'No':
        break
    to_turn = + 1
    print_sheet(sheet)
