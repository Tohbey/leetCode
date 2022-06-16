from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 3:
            return True
        
        low = 0
        high = int(sqrt(c))
        
        while low <= high:
            val = low * low + high * high
            if val == c:
                return True
            elif val < c:
                low += 1
            else:
                high -= 1
        
        return False
    
res = Solution()
print(res.judgeSquareSum(5))