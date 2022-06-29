def solution(arr):
    longest_sub, curr_count = 0, 1

    for i in range(len(arr)):
        if i + 1 in range(len(arr)):
            if arr[i] < arr[i + 1]:
                curr_count += 1
                continue

            if arr[i] > arr[i + 1] or arr[i] == arr[i + 1]:
                if longest_sub < curr_count:
                    longest_sub = curr_count
                curr_count = 0

    return longest_sub


"""     while (last < len(arr) - 1):
        if arr[first] < arr[last]:
            curr_count += 1
            last += 1
            first += 1
            continue

        if arr[first] > arr[last] or arr[first] == arr[last]:
            first = last
            if longest_sub < curr_count:
                longest_sub = curr_count
            curr_count = 0
            continue
 """

A = [-1, 3, 4, 5, 2, 2, 3, 2, 2, 2, 4, 6, 7, 8, 12, 67, 8, 8, 3, 4, 6, 7]
print(solution(A))