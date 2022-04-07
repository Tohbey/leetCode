from pip import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        if(len(nums) >= 3):
            return nums[-3]
        else:
            return nums[-1]


res = Solution()
nums = [2,1]
print(res.thirdMax(nums))