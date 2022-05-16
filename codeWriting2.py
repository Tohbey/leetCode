from typing import List

class Solution:
    def minimizeSum(self,  nums: List[int]) -> int:
        sum = 0
        result = []
        left = 0
        lenght = len(nums)
        for i in range(0, len(nums)):
            while left < lenght:
                sum += abs(nums[i] - nums[left])
                left +=1
            left = 0
            result.append(sum)
            sum = 0

        minIndex = result.index(min(result))

        return nums[minIndex]

        

res = Solution()
nums = [2,3]
res.minimizeSum(nums)


