def spiral_traverse(matrix):
    if len(matrix) == 0:
        return 'Empty array received'

    if len(matrix) == 1:
        return matrix

    col = 0
    row = 0

    available_rows = len(matrix) - 1
    available_cols = len(matrix[0]) - 1

    row_limit = len(matrix)
    col_limit = len(matrix[0])

    row_lim_rev = -1
    col_lim_rev = -1

    visited = []

    while available_rows > 0:

        col = move_right(row, col, col_limit, visited, matrix)
        row += 1
        row = move_down(row, col, row_limit, visited, matrix)

        available_rows -= 1

        row_lim_rev += 1

        col -= 1
        col = move_left(row, col, col_lim_rev, visited, matrix)
        row -= 1
        row = move_up(row, col, row_lim_rev, visited, matrix)
        col += 1

        available_cols -= 1

        col_limit -= 1
        row_limit -= 1
        col_lim_rev += 1
        row_lim_rev += 1

    return visited


def move_right(row, col, col_limit, visited, matrix):
    while col < col_limit:
        visited.append(matrix[row][col])
        col += 1

    return col-1


def move_down(row, col, row_limit, visited, matrix):
    while row < row_limit:
        visited.append(matrix[row][col])
        row += 1

    return row - 1


def move_left(row, col, col_lim_rev, visited, matrix):
    while col > col_lim_rev:
        visited.append(matrix[row][col])
        col -= 1

    return col + 1


def move_up(row, col, row_lim_rev, visited, matrix):
    while row > row_lim_rev:
        visited.append(matrix[row][col])
        row -= 1

    return row + 1


matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(spiral_traverse(matrix))
