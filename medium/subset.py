from turtle import right
from unittest import result
from pip import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        print(nums)
        result = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        print(result)
      

res = Solution()
nums = [1, 2, 3]
res.subsets(nums)