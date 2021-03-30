""" def solution(arr):
    if len(arr) == 0:
        return 0

    singles = set(arr)

    while len(singles) > 0:
        target = singles.pop()
        if arr.count(target) % 2 == 1:
            return target """


def solution(arr):

    if len(arr) == 0:
        return 0

    hash = dict()

    for i in range(len(arr)):
        hash[arr[i]] = hash.get(arr[i], 0)+1

    for i in hash:
        if hash[i] % 2 != 0:
            return i

    return 'No singles'


A = [9, 3, 9, 3, 9, 7, 9]
ans = solution(A)

print(ans)