class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n) or O(nlogn)
        # nums is sorted in ascending order. ???
        i = 0
        while i < len(nums):
            curr, count, initial = nums[i], 0, i
            while i < len(nums) and curr == nums[i]:
                i += 1
                count += 1
            
            if count > 2:
                i = initial + 2
            else:
                i = initial + 1
            
            while count > 2:
                del nums[initial + 2]
                count -= 1
        
            
                
