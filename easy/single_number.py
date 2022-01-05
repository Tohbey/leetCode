from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
           counts = nums.count(nums[i])
           if counts == 1:
               return nums[i]


nums = [2,2,1,1,4]
res = Solution()
print(res.singleNumber(nums))