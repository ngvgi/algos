def count_occur(A):

    if len(A) == 0:
        return 0
    
    if len(A) == 1:
        return A
    
    count_arr = [None] * len(A)

    for i in range(max(A)):
        count = 1
        for j in range(i+1, len(A)):
            if A[j] == A[i]:
                count += 1
        if i <= len(count_arr) - 1:
            count_arr[i] = count
            


    return count_arr


A = [9,6,4,2,9,3]

# print(count_occur(A))

def count_occur_dict_style(A):
    if len(A) == 0:
        return 0

    if len(A) == 1:
        return A
    
    hash = dict()
    
    for num in A:
        hash[num] = hash.get(num, 0) + 1
    
    return hash


A = [9,6,4,2,9,3]

print(count_occur_dict_style(A))