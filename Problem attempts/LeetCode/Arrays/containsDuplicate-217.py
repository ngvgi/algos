class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) <=1:
            return False

        if len(set(nums)) == len(nums):
            return False   
        return True
            
            
nums = [1,2,3,4]
print(Solution().containsDuplicate(nums))