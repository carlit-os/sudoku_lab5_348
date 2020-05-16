import common


# helpful, but not needed
class variables:
    counter = 0


def is_board_full(board):
    for y in board:
        for x in y:
            if x == 0:
                return False
    return True


def empty_spots(board):
    # returns list of empty spaces in assigned order
    result = []
    for row, y in enumerate(board):
        for col, x in enumerate(y):
            if x == 0:
                result.append((row, col))
    return result


def is_valid(board, spot, value):
    return common.can_yx_be_z(board, spot[0], spot[1], value)


def recur_backtrack(sudoku):
    variables.counter += 1
    if is_board_full(sudoku):
        return True
    else:
        for spot in empty_spots(sudoku):
            for v in range(1, 10):
                if is_valid(sudoku, spot, v):
                    sudoku[spot[0]][spot[1]] = v
                    if recur_backtrack(sudoku):
                        return True
                    sudoku[spot[0]][spot[1]] = 0  # remove from board
            return False


def sudoku_backtracking(sudoku):
    variables.counter = 0
    # put your code here
    recur_backtrack(sudoku)

    return variables.counter


def sudoku_forwardchecking(sudoku):
    variables.counter = 0
    # put your code here
    return variables.counter
