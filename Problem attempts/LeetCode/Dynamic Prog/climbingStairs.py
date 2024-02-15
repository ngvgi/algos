# Leetcode 70

class Solution:
    def climbStairs(self, n: int, cache={}) -> int:        
        if n in cache: return cache[n]

        if n == 1: return 1
        if n == 2: return 2

        cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return cache[n]


print(Solution().climbStairs(80))