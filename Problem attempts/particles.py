# def solution(A):
#     periods = 0
#     i = 0

#     while i+2 <= len(A) - 1:
#         if abs(A[i] - A[i+1]) == abs(A[i+1] - A[i+2]):
#             periods += 1
#             i += 2
#             continue
#         i += 1

#     return periods


# print(solution([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))
""" 
steps:

    1. check if array has at least 3 particles
    2. for particle in particles:
        2.1 start a loop at first particle
        2.2 start a nested loop at second particle:
            if difference between the second and its next particle is the same:
                update periods counter
                move to the fourth particle
                ...
            else
                break out of this nested loop to update the first particle counter
    3. return periods counter, or -1 if it's above 1Billion

"""


def solution(A):
    periods = 0
    # min of 3 particles must be considered for a period to be counted as stable
    if len(A) < 3:
        return 0
    # outer loop checks from first particle to third-last particle
    for i in range(len(A) - 2):
        # this loop checks from the second particle to the second-last particle
        for j in range(i + 1, len(A) - 1):
            if A[j + 1] - A[j] == A[i + 1] - A[i]:
                periods += 1
                continue
            break
    return periods if periods < 1000000000 else -1


print(solution([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))
