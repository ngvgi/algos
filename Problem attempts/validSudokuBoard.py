def isValidSudoku(board):
    return valid_cols(board) and valid_rows(board) and valid_subgrid(board)


def valid_cols(board):
    val_count = 0
    char_set = set()

    for row in range(9):
        for col in range(9):
            if board[col][row] != '.':
                val_count += 1
                char_set.add(board[col][row])

        if len(char_set) < val_count:
            return False

        char_set.clear()
        val_count = 0

    return True


def valid_rows(board):
    val_count = 0
    char_set = set()

    for row in range(9):
        for col in range(9):
            if board[row][col] != '.':
                val_count += 1
                char_set.add(board[row][col])
        if len(char_set) < val_count:
            return False

        char_set.clear()
        val_count = 0

    return True


def valid_subgrid(board):
    row_start = 0
    col_start = 0
    char_set = set()
    row_limit = row_start + 3
    col_limit = col_start + 3
    val_count = 0

    subgrid = 1

    while subgrid <= 9:
        for row in range(row_start, row_limit):
            for col in range(col_start, col_limit):
                if board[row][col] != '.':
                    val_count += 1
                    char_set.add(board[row][col])

        if len(char_set) < val_count:
            return False

        row_start += 3
        row_limit = row_start + 3
        val_count = 0
        char_set.clear()
        subgrid += 1

        if row_start == 9:
            row_start = 0
            row_limit = row_start + 3
            col_start += 3
            col_limit = col_start + 3

        if col_start == 9:
            break

    return True


board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
