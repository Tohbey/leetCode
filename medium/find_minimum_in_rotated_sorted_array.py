from pip import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        val = self.findPos(nums)
        print(nums[val])
        return nums[val]
        
    def findPos(self,nums) -> int:
        rem=0
        if nums[-1]>nums[0]:
            return rem
        else:
            start,end,val=0,len(nums)-1,nums[-1]
            
            while start<=end:
                
                mid=(start+end)//2
                if nums[mid]>val:
                    start=mid+1
                else:
                    rem=mid
                    end=mid-1
            return rem
        
res = Solution()
nums = [3,4,5,1,2]
res.findMin(nums)