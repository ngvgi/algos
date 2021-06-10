def solution(X, Y, D):
    if X == Y:
        return 0

    Y -= X

    jumps = Y // D

    if Y % D > 0:
        jumps += 1

    return jumps


print(solution(1, 5, 2))
