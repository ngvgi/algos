def solution(A):
    if len(A) == 0:
        return 1
    if len(A) == 1 and 1 not in A:
        return 1
    
    vals = set(filter(lambda x: (x > 0), A))

    
    if len(vals) == 0 or len(vals) == 1 and 1 not in vals:
        return 1

    min_positive = 1
    i = 0

    while i<len(vals)-1:
        if min_positive not in vals:
            return min_positive       
        min_positive+=1
        if min_positive in vals:
            i+=1
            continue        
        else: return min_positive
    
    min_positive +=1

    return min_positive

# A = [-1, 3]
# A = [1, 3, 6, 4, 1, 2]
# A = [1, 3, 6, 4, 1, 5,2]
# A = [-2,3,2,-22,2,1,43,234234,99292, ]
A =[-1000000, 1000000]
print(solution(A))