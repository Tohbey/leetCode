from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            counts = nums.count(nums[i])
            if counts > 1:
                return True
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        flag = False
        for i in range(len(nums) - 1):
            if(nums[i] == nums[i+1]):
                flag = True
                return flag
        return flag

