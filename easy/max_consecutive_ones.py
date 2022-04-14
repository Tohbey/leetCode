from re import L
from pip import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, curr_count = 0, 0
        left = 0
        while left < len(nums):
            while left < len(nums) and nums[left] == 1:
                left += 1
                curr_count += 1
            
            max_count, curr_count = max(max_count, curr_count), 0
            left +=1

        
        return max_count



res = Solution()
nums = [1,0,1,1,0,1]
result = res.findMaxConsecutiveOnes(nums)
print(result)