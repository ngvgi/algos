def check(row, col, matrix):
    mines = 0
    up = row - 1 if row - 1 >= 0 else 0
    down = row + 1 if row + 1 <= len(matrix) - 1 >= 0 else len(matrix) - 1
    left = col - 1 if col - 1 >= 0 else 0
    right = col + 1 if col + 1 <= len(matrix[0]) - 1 else len(matrix[0]) - 1

    for i in range(up, down + 1):
        for j in range(left, right + 1):
            if matrix[i][j] == 'B' and row != i and col != j:
                mines += 1
    return mines


def solution(N, bomb_rows, bomb_cols):
    ans = [[0 for i in range(N)] for i in range(N)]

    for i in range(len(bomb_rows)):
        ans[bomb_rows[i]][bomb_cols[i]] = 'B'

    for i in range(len(ans)):
        for j in range(len(ans[0])):
            if ans[i][j] == 'B':
                continue
            ans[i][j] = check(i, j, ans)

    return ans


print(solution(3, [2, 1, 0, 2], [0, 2, 1, 2]))