from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        
        for k in nums:
            if k in majority:
                majority[k] += 1
            else:
                majority[k] = 1
                
        for k in majority:
            maj_key = max(majority, key=majority.get)
            return maj_key

res = Solution();
nums = [2,2,1,1,1,2,2];

print(res.majorityElement(nums));
