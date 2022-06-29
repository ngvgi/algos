""" 
steps:
    1. Count how many times each character appears
    2. Check how many characters have a similar count of appearances
    3. If two characters share an appearance count: 
           3.1 - pick one and reduce it's appearance count
           3.2 - update the deletions counter
           3.2 - repeat 3.1 until no two characters share an appearance count
    4. Return the deletions
"""


def solution(s):
    # store how many times each character appears
    hash = {}
    for char in s:
        hash[char] = hash.get(char, 0)+1

    deletions = 0
    occurrences_arr = sorted([i for i in hash.values()])
    for i in range(len(occurrences_arr)-1):
        # if two characters appear the same number of times, reduces the appearance count of one of them
        if occurrences_arr[i] == occurrences_arr[i+1]:
            occurrences_arr[i] -= 1
            deletions += 1
            j = i-1
            k = i
            # if reducing current char count makes current element appear a similar number of times as an element
            # that was previously seen, update the current element to appear less times than all
            # previous elements
            while occurrences_arr[k] and occurrences_arr[k] == occurrences_arr[j]:
                occurrences_arr[j] -= 1
                j -= 1
                k -= 1
                deletions += 1

    return deletions


print(solution('hello'))
