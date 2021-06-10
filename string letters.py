def solution(A):
    if len(A) == 0 or len(A) == 1:
        return 0

    A_count, removables, Bs_after_As, Bs_before_As = 0, 0, 0, 0

    for i in range(len(A)):
        if i == 0:
            if A[i] == 'B':
                Bs_before_As += 1
                continue
            else:
                A_count += 1
                continue

        if A[i] == 'B' and A_count == 0:
            Bs_before_As += 1
        if A[i] == 'A' and Bs_before_As > 0:
            removables = Bs_before_As
            Bs_before_As = 0
            A_count += 1
        if A[i] == 'B' and A_count > 0:
            Bs_after_As += 1
        if A[i] == 'A' and Bs_after_As > 0:
            removables += 1

    return removables


A = 'AABABB'
ans = solution(A)
print(ans)