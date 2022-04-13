from pip import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        b = set([x for x in range(1, len(nums)+1)])
        return list(b.difference(a))

res = Solution()
nums = [2,2]
# nums = [4,3,2,7,8,2,3,1]
ans = res.findDisappearedNumbers(nums)
print(ans)