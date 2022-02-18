class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start < end:
            current = start + (end- start)//2

            if isBadVersion(current) == True:
                end = current
            else:
                start = current + 1

        
        return end