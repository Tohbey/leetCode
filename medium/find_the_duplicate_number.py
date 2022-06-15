from pip import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashtable = {}
        for num in nums:
            if num in hashtable:
                return num
            else:
                hashtable[num] = 1
        
            
nums = [1,3,4,2,2]
res = Solution()
print(res.findDuplicate(nums))