class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
                
        while l <= r:
            middle = (l+r) // 2
            
            if nums[middle] == target:
                return middle

            if target > nums[middle]:
                l = middle + 1
            else:
                r = middle - 1
        
        return l 
            

