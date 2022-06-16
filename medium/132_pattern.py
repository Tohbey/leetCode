from pip import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        start, end = 0,3
        while end <= len(nums):
            if nums[start] < nums[end-1] and nums[end-1] < nums[start+1]:
                return True
            else:
                start+=1
                end+=1
        
        return False
    
    def find132pattern1(self, nums: List[int]) -> bool:
        stack = []  # [nums,minleft]
        minCurr = nums[0]        
        for n in nums[1:]:
            while stack and stack[-1][0] <= n:
                stack.pop()                
            if stack and stack[-1][1] < n:
                return True 
            stack.append([n,minCurr])
            minCurr = min(n, minCurr)
        return False
        
res = Solution()
nums = [3,5,0,3,4]
print(res.find132pattern(nums))