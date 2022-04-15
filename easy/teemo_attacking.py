from pip import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = duration
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i - 1]
            if diff <= duration:
                total += diff
                print(total)
            else:
                total += duration
        return total

                


res = Solution()
timeSeries = [1,4]
duration = 2
res.findPoisonedDuration(timeSeries, duration)