def solution(A):
    if len(A) == 0:
        return 0

    if len(A) == 1 and 1 not in A:
        return 0
    if len(A) == 1 and 1 in A:
        return 1

    # to ensure number appears only once
    hash = dict()
    for i in range(len(A)):
        hash[A[i]] = hash.get(A[i], 0) + 1
    appearances = hash.values()
    unique_appearances = set(appearances)
    if len(unique_appearances) > 1:
        return 0
    
    #main code

    loops = 0
    elements = set(A)
    largest = max(elements)

    if len(elements) == 1 or 1 not in elements:
        return 0

    while (loops < len(elements) - 1):
        largest -= 1
        if largest in elements:
            loops += 1
            continue
        else:
            return 0

    return 1


A = [2, 3]
print(solution(A))
