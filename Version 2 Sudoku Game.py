grid_numbers: int = [[None for c in range(9)] for r in range(9)]

def intialise_0():
    row: int = 0
    while row < 9:
        column: int = 0
        while column < 9:
            grid_numbers[row][column] = 0
            column: int = column + 1
        row: int = row + 1

def intialise_8():
    row: int = 0
    while row < 9:
        column: int = 0
        while column < 9:
            grid_numbers[row][column] = 8
            column: int = column + 1
        row: int = row + 1

def printing():
    row: int = 0
    while row < 9:
        column: int = 0
        while column < 9:
            print(grid_numbers[row][column], end=" ")
            column: int = column + 1
        print()
        row: int = row + 1

def check_if_filled():
    grid_filled_verifier: bool = True

    row: int = 0
    while row < 9:
        column: int = 0
        while column < 9:

            if grid_numbers[row][column] == 0:
                grid_filled_verifier = False

            column = column + 1
        row = row + 1

    if grid_filled_verifier == False:
        print("Sudoku Grid has not been successfully filled!")

    else:
        print("Sudoku Grid has been successfully filled!")
    
intialise_0()
printing()
check_if_filled()

intialise_8()
printing()
check_if_filled()
