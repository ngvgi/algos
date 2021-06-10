""" 
# this solution scored 66%

def solution(N, A):
    counters = [0] * N
    largest = 0

    for i in range(len(A)):
        if 1 <= A[i] <= N:
            counters[A[i] - 1] += 1
            if counters[A[i] - 1] > largest:
                largest = counters[A[i] - 1]
        elif A[i] == N + 1:
            counters = [largest for k in counters]
        i += 1

    return counters


"""


def solution(N, A):
    counters = [0 for i in range(N)]
    curr_max = 0
    curr_min = 0

    for i in A:
        if 1 <= i <= N:
            if curr_min > counters[i - 1]:
                counters[i - 1] = curr_min

            counters[i - 1] += 1

            if curr_max < counters[i - 1]:
                curr_max = counters[i - 1]

        else:
            curr_min = curr_max

    for i in range(N):
        if counters[i] < curr_min:
            counters[i] = curr_min

    return counters


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
