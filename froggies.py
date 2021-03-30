def check_right(arr, i):
    if i >= len(arr) - 1:
        return 0
    if (arr[i+1] < arr[i]):
        return 0
    farthest_right = i
    while(arr[i+1] >= arr[i]):
        i += 1
        if i > len(arr)-1:
            break
        farthest_right = i
        if farthest_right + 1 > len(arr) - 1:
            return farthest_right
    return farthest_right


def check_left(arr, i):
    if (i == 0):
        return 0
    if (arr[i-1] < arr[i]):
        return i
    farthest_left = i
    while(arr[i-1] >= arr[i]):
        farthest_left = i-1
        i = farthest_left
        if farthest_left - 1 < 0:
            return farthest_left
    return farthest_left


def solution(blocks):
    max_distance = 0
    unique_values = set(blocks)
    if(len(unique_values) == 1):
        return len(blocks)
    for i in range(len(blocks)):
        left_leap = check_left(blocks, i)
        right_leap = check_right(blocks, i)
        distance = (right_leap - left_leap) + 1
        if (distance > max_distance):
            max_distance = distance
    return max_distance


a = [2, 6, 8, 9]
b = [1, 6, 5, 5, 2, 6]
c = [4, 4, 4, 4, 4]
d = [1, 2, 4, 3]
e = [2, 4, 1, 3, 9]

sol = solution(e)
print(sol)
