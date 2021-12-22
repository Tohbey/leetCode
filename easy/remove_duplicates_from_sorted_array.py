class Solution:
    def removeDuplicates(self, nums: int):
        # expectedNums = set()
        # for i in nums:
        #     expectedNums.add(i)
        
        # nums = list(expectedNums)
        # return nums
    
        k = 1
        i = j = k
        n = len(nums)
        if n<=k:
            return n
        while(j<n):
            if nums[j]!= nums[i-k]:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i
    
nums = [0,0,1,1,1,2,2,3,3,4]
res = Solution()
print(res.removeDuplicates(nums))