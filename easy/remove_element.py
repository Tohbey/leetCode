from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        if len(nums) == 0:
            return 0
        
        while i >= 0:
            if nums[i] is val:
                nums.pop(i)
                i = len(nums)
            
            i-=1
                 
        return len(nums)