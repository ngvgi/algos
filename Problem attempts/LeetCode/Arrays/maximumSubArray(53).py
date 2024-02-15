class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        
        wholeArrSum = sum(nums)
        start = 0
        stop = 1
        currSum = nums[0]
        maxSum =0

        while start < len(nums) - 1:
            currSum += nums[stop]
            maxSum = max(maxSum, wholeArrSum)

            if currSum <= wholeArrSum:
                start +=1 
                stop = start + 1
                currSum = nums[start]

                if start == len(nums) - 1:
                    return max(currSum, maxSum)
                
            else:
                if currSum > maxSum:
                    maxSum = currSum
                stop += 1
                if stop > len(nums) - 1:      
                    return max(maxSum, wholeArrSum)


"""
Correct solution
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        running_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            running_sum = max(running_sum + nums[i], nums[i])
            max_sum = max(running_sum, max_sum)
        
        return max_sum

       

# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
# nums = [-2,1,-3,4,-1,2,1,-5,4]

print(Solution().maxSubArray(nums))