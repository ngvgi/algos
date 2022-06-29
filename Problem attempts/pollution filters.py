def solution(A):

    if len(A) == 0:
        return 0

    filters = 0
    pollution_sum = sum(A)
    half_pol = pollution_sum / 2

    while (pollution_sum > half_pol):
        largest_pol = max(A)
        A[A.index(largest_pol)] = largest_pol / 2
        filters += 1
        pollution_sum = sum(A)

    return filters


A = [13, 5, 8, 3, 1]

print(solution(A))
