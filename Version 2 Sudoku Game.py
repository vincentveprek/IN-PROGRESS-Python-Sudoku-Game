grid_numbers = [[None for c in range(9)] for r in range(9)]

def intialise():
    row = 0
    while row < 9:
        column = 0
        while column < 9:
            grid_numbers[row][column] = 0
            column = column + 1
        row = row + 1

def printing():
    row = 0
    while row < 9:
        column = 0
        while column < 9:
            print(grid_numbers[row][column], end=" ")
            column = column + 1
        print()
        row = row + 1

intialise()
printing()
