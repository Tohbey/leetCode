from pip import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}

        for i, num in enumerate(nums):
            if num in freq.keys():
                j = freq[num]
                if abs(i - j) <= k:
                    return True
         
            freq[num] = i         
                    
        return False  


res = Solution()
nums = [1, 2, 3, 1, 2, 3]
print(res.containsNearbyDuplicate(nums, 2))
