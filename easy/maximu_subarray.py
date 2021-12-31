from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub= nums[0]
        currrentSum = 0
        for n in nums:
            if currrentSum < 0:
                currrentSum = 0
            
            currrentSum += n
            maxsub = max(maxsub, currrentSum)
        
        return maxsub