from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        nums.sort()
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        for i in range(len(nums) - 1):
            j, k = i + 1, len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if current == target:
                    return target
                if abs(current - target) < abs(result - target):
                    result = current                
                if current > target:
                    k -= 1
                else:
                    j += 1
        return result

nums = [-1,2,1,-4]
target = 1
res = Solution()
print(res.threeSumClosest(nums, target))
            
                
                