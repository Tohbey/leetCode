from functools import cmp_to_key
from pip import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        print(nums)
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))


res = Solution()
nums = [3, 30, 34, 5, 9]
res.largestNumber()