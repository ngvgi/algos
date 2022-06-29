import math
def solution(N):
    count = 0
    root = math.sqrt(N)
    limit = math.floor(root)
    i = 1

    # get **PAIRS** of factors
    while i <= limit:
        if N%i == 0:
            count+=1
        i+=1
    
    count *= 2
    
    if math.floor(root) == math.ceil(root):
        return count - 1
    
    return count 


print(solution(16))