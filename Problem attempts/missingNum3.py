""" def solution(A):
    if len(A) == 1 and 1 not in A:
        return 1

    if len(A) == 1 and 1 in A:
        return 2

    elements = set(A)
    if max(elements) < 1 or 1 not in elements:
        return 1

    i = 0
    min_el = 0
    current_min = 0

    while i < len(A) - 1:
        element = A[i]
        if element < 1:
            i += 1
            continue
        if element > 1 and element+1 not in A:
            current_min = element + 1
            if min_el == 0 or current_min < min_el:
                min_el = current_min 
        i+=1
    return min_el


# A = [-1, -3, 33, 432, 2, 1, 53]
A = [1, 3, 6, 4, 1, 2]
sol = solution(A)
print(sol)
 """
""" class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = ''
        words = s.split()

        while len(words)>0: 
            addable = words[-1] 
            reversed_words = reversed_words + addable + " "
            words=words[:-1]     

        reversed_words.strip(' ')       


        return reversed_words
        

A = 'the sky is blue'
# A = ' '
# A = ' the sky is blue '
solution = Solution()


print(solution.reverseWords(A))
 """


""" class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        S1, S2, new_s1 = '',  '', ''

        for i in range(len(s1)):
            if s1[i] not in s2:
                new_s1 = s1.replace(s1[i], '')

        S1 = new_s1*n1 if new_s1 != '' else s1*n1
        S2 += s2*n2

        count = len(S1) // len(S2)
        return count


solution = Solution()
s1 = "aaab"
n1 = 2
s2 = "ab" 
n2 = 1

sol = solution.getMaxRepetitions(s1,n1, s2, n2)
print(sol) """

def solution(A):
    if len(A) == 0 or len(A) == 1 :
        return 0
    
    if len(A) == 2 and A[0] < A[1]:
        return 1
    
    if len(A) == 2 and A[0] > A[1]:
        return 0
    
    
    first = 0
    count = 0
    second = 1

    while first < len(A) -1: 
        if A[second] > A[first]:
            count +=1
        second +=1 
        if second == len(A):
            first+=1
            second = first + 1
        
    
    return count

# A = [0,1,0,1,1]
A = [1,1,1,1,1]
# A = [0,0,0,0,1]
sol = solution(A)
print(sol)
