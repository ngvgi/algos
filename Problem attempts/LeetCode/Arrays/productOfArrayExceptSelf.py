class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_pass= [1] * len(nums)
        right_pass = [1] * len(nums)
        productArr=[None] * len(nums)


        for i in range(len(nums) - 1):
            product = 1
            for j in range(i+1, len(nums)):
                product *= nums[j]
                j+=1
            right_pass[i] = product



        for i in range(len(nums) - 1, -1, -1):
            product = 1
            for j in range(i-1, -1, -1):
                product *= nums[j]
                j-=1
            left_pass[i] = product
        


        for i in range(len(right_pass)):
            productArr[i] = right_pass[i] * left_pass[i]

        return productArr
            



nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))