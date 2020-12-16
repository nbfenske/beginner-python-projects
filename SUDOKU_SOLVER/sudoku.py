
def find_next_empty(puzzle):
    # find next row, col on the puzzle that is not filled yet --> represented by -1

    # 0-8 for the indicies
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None # no more spaces left!

def is_valid(puzzle, guess, row, col):
    # find if there are any conflicts in the current state
    # row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # 3x3 matrix, find the start col/row for that submatrix
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    
    row, col = find_next_empty(puzzle)

    if row is None:
        return True # puzzle has been solved!
    
    # make a guess for the next available space, try all until we find a combination that works
    for guess in range(1,10): #1-9
        if is_valid(puzzle, guess, row, col):
            # place guess if valid
            puzzle[row][col] = guess
            # recursively call this to find the correct solution
            if solve_sudoku(puzzle):
                return True
        # backtrack if our guess was wrong
        puzzle[row][col] = -1 # reset value

    # unsolveable if we reach this point
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)