def findKthLargest(nums, k: int) -> int:
        if k == len(nums):
            return min(nums)
        
        if k == 1:
            return max(nums)
        
        store = []

        for num in nums:
            if len(store) == 0 or num > max(store):
                store.append(num)
                continue
            
            if num < store[0]:
                store[:0] = [num]
        
        return store[len(store)- k]


nums = [3,2,1,5,6,4]
k = 3

print(findKthLargest(nums, k))