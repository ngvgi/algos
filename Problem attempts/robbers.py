from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        safe_house, immediate_neighbour, max_stealings = 0, 0, 0

        for curr_house in nums:
            max_stealings = max(curr_house + safe_house, immediate_neighbour)
            safe_house = immediate_neighbour
            immediate_neighbour = max_stealings

        return max_stealings


nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
