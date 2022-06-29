from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False

        hash = dict()
        multi_occur = list()
        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        for key, val in hash.items():
            if val > 1:
                multi_occur.append(key)
        print(multi_occur)
        for num in multi_occur:
            i = nums.index(num)
            j = nums.index(num, i + 1)

            if abs(i - j) <= k:
                return True
            continue

        return False


Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)
