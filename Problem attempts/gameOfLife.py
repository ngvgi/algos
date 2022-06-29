def gameOfLife(board):
    print('Old board: {}'.format(board))

    rows = len(board)
    cols = len(board[0])
    travelX = [-1, -1, -1, 0, 1, 1, 1, 0]
    travelY = [-1, 0, 1, 1, 1, 0, -1, -1]
    total = 0
    deductibles = {
        0: [],
        1: []
    }

    for row in range(rows):
        for col in range(cols):
            total = 0
            for i in range(len(travelX)):
                neighbourX = row + travelX[i]
                neighbourY = col + travelY[i]
                if neighbourX < 0 or neighbourX > rows - 1 or neighbourY < 0 or neighbourY > cols - 1:
                    continue
                total += board[neighbourX][neighbourY]

            if total < 2:
                deductibles[0].append((row, col))
            if total == 3 and board[row][col] == 0:
                deductibles[1].append((row, col))
            if total >= 2 and total <= 3 and board[row][col] == 1:
                deductibles[1].append((row, col))
            if total > 3 and board[row][col] == 1:
                deductibles[0].append((row, col))

    for i in deductibles[0]:
        board[i[0]][i[1]] = 0

    for i in deductibles[1]:
        board[i[0]][i[1]] = 1

    print('New board: {}'.format(board))

    return


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(gameOfLife(board))
