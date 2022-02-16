from pip import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        current = 0
        nextVal = 1
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]

        ranges = []
        while nextVal < n:
            while nextVal < n and nums[nextVal] == nums[nextVal - 1] + 1:
                nextVal += 1
            if current + 1 == nextVal:
                ranges.append(str(nums[current]))
            else:
                ranges.append(str(nums[current])+"->"+str(nums[nextVal - 1]))
            current = nextVal
            nextVal = nextVal + 1

        if current < n and current + 1 == nextVal:
            ranges.append(str(nums[current]))
        return ranges


nums = [0,1,2,4,5,7]
res = Solution()
print(res.summaryRanges(nums))            