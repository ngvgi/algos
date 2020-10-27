""" def solution(arr, k):
    if len(arr) == 1 or k == len(arr) or k == 0 or len(arr) == 0:
        return arr

    if k > len(arr):
        k = k % len(arr)
        if k == 0:
            return arr

    n = 0

    while n < k:
        shifted_arr = [0]*len(arr)
        shifted_arr[0] = arr[-1]

        for i in range(len(arr)-1):
            shifted_arr[i+1] = arr[i]

        arr = shifted_arr

        n += 1

    return shifted_arr


A = [-1, -2, -3, -4, -5, -6]
K = 8000000000000
print(solution(A, K))
"""


def solution(arr, k):
    if len(arr) == 1 or k == len(arr) or k == 0 or len(arr) == 0:
        return arr

    if k > len(arr):
        k = k % len(arr)
        if k == 0:
            return arr

    shifted_arr = [None]*len(arr)

    for i in range(len(arr)):
        if i + k < len(arr):
            shifted_arr[i+k] = arr[i]

        else:
            shifted_arr[(i+k) % len(arr)] = arr[i]
        i += 1

    return shifted_arr


A = [3, 8, 9, 7, 6, 88, 134]
K = 79

print(solution(A, K))
