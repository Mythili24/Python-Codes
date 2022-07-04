def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j])
        print()


def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None


def is_valid(grid, num, row, col):
    for i in range(9):
        if grid[row][i] == num:
            return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):

    row, col = find_empty_location(grid)

    if row is None:
        return True

    for num in range(1, 10):
        print('num:', num)
        if is_valid(grid, num, row, col):

            grid[row][col] = num

            if solve_sudoku(grid):
                return True

        grid[row][col] = 0

    return False


if __name__ == "__main__":

    grid = [[0 for x in range(9)] for y in range(9)]

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if (solve_sudoku(grid)):
        print_grid(grid)
    else:
        print("No solution exists")