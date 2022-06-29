def solution(A):
    pairs = 0
    odds = [
        x if x not in A and x % 2 == 1 else 'Booked'
        for x in range(1, A[0], 2)
    ]
    evens = [
        x if x not in A and x % 2 == 0 else 'Booked'
        for x in range(2, A[0] + 1, 2)
    ]

    evens[-1] = A[0] if A.count(A[0]) == 1 else 'Booked'

    i = 0
    while i < len(odds):
        if odds[i] != 'Booked' and evens[i] != 'Booked':
            pairs += 1
        if i < len(odds) - 1:
            if odds[i] != 'Booked' and odds[i + 1] != 'Booked':
                pairs += 1
            if evens[i] != 'Booked' and evens[i + 1] != 'Booked':
                pairs += 1

        i += 1

    return pairs


# A = [16, 3, 4, 8, 10, 12]
A = [12, 2, 6, 7, 11]
ans = solution(A)
print(ans)