def solution(A):
    longest_sub = 0
    len_substring = 0
    a_count = 0
    b_count = 0
    consec_b = 0
    consec_a = 0
    start_idx = 0
    stop_idx = 0

    for i in range(len(A)):
        if i > 0:
            if i == len(A) - 1 and start_idx == 0:
                return len(A)

            if i + 1 == len(A) - 1 and start_idx > 0:
                if A[i] == A[i - 1] and A[i] == i + 1:
                    stop_idx = i
                    len_substring = (stop_idx - start_idx) + 1
                    if len_substring > longest_sub:
                        longest_sub = len_substring
                        return longest_sub
                else:
                    stop_idx = i + 1
                    len_substring = (stop_idx - start_idx) + 1
                    if len_substring > longest_sub:
                        longest_sub = len_substring
                        return longest_sub

            if A[i] == 'A' and A[i - 1] == 'A':
                consec_a = a_count + 1
                a_count += 1
                if consec_a == 3:
                    stop_idx = i - 1
                    len_substring = (stop_idx - start_idx) + 1
                    if longest_sub < len_substring:
                        longest_sub = len_substring
                    start_idx = stop_idx
                    stop_idx = 0
                    consec_a = 0
                    a_count = 0
                    b_count = 0
                    continue
            else:
                if A[i] == 'A':
                    a_count += 1
                    b_count = 0
                    consec_b = 0
                    continue

            if A[i] == 'B' and A[i - 1] == 'B':
                consec_b = b_count + 1
                b_count += 1
                if consec_b == 3:
                    stop_idx = i - 1
                    len_substring = (stop_idx - start_idx) + 1
                    if longest_sub < len_substring:
                        longest_sub = len_substring
                    start_idx = stop_idx
                    stop_idx = 0
                    consec_b = 0
                    b_count = 0
                    a_count = 0
                    continue
            else:
                if A[i] == 'B':
                    b_count += 1
                    a_count = 0
                    consec_a = 0
                    continue

        else:
            if A[i] == 'A':
                a_count += 1
                continue
            if A[i] == 'B':
                b_count += 1

        i += 1

    return len_substring


# A = 'BAAABBABBB'
# A = 'BABBA'
# A = 'ABAAAA'
# A = 'AAABABABAAAAABABAAAAAB'
# A = 'AAAAAABABABAABABAABABAAABABBAABAABABAABBBBAABABABBAABAABBAAB'
A = 'AAABABABBAABABABAABAABAABABABABBAABABABAABAABABA'

print(solution(A))