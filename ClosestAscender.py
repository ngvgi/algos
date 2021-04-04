""" 
    Input: Array A
    Output: Array R, 
    Problem: 
        Given array A, get the closest ascender to each element. The closest ascender is the nearest
        element that is greater than the current element. 
        Once you get the closest ascender to element at i, in array R, at index i, set this value to 
        be the abs(i - k), where k is the index of the closest ascender
    
    Approach:
        1. Initialize array R, and fill it with 0s. This will help us only write to it if we find an
            ascender.
        2. Check where we currently are:
                    if we are at index 0:
                        only run a pass to the right,
                    if we are at the last index:
                        only run a pass to the left
                    if we are anywhere in the middle:
                        run both a left and right pass
        3. If we find the ascender:
                    check if there is an ascender in the opposite direction
                    if there is an ascender in the opposite direction:
                        see difference between the current ascender and the one in the opposite direction
                        closest ascender = smallest difference of the two
                        set R[i] to abs(closest ascender - i)
            if we don't find the ascender:
                continue with iteration since array R already was initialized and prefilled with 0s


                        
"""


def solution(A):
    left_pass = [0] * len(A)
    right_pass = [0] * len(A)

    current_idx = 0
    right_idx = current_idx + 1
    while current_idx < len(A):
        if right_idx == len(A):
            break
        if A[right_idx] > A[current_idx]:
            right_pass[current_idx] = abs(right_idx - current_idx)
            current_idx += 1
            right_idx = current_idx + 1
            continue
        right_idx += 1

    current_idx = len(A) - 1
    left_idx = current_idx - 1
    while current_idx > 0:
        if left_idx == -1:
            current_idx -= 1
            left_idx = current_idx - 1
            continue
        if A[left_idx] > A[current_idx]:
            left_pass[current_idx] = abs(left_idx - current_idx)
            current_idx -= 1
            left_idx = current_idx - 1
            continue
        left_idx -= 1

    R = [min(a, b) if a > 0 else b for a, b in zip(left_pass, right_pass)]

    return R


# A = [4, 3, 1, 4, -1, 2, 1, 0, 1, -3, -4, 2, 1, 0, 3, 5, 7]
A = [4, 3, 1, 4, -1, 2, 1, 5, 7]
# A = [4, 3, 1, 0, 2]
ans = solution(A)
print(ans)
