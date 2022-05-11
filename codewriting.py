import numbers
from pip import List


class Solution:
    def codeWriting(self, numbers: List[int], left:int, right:int) -> List[bool]:
        result = [False]* len(numbers)
        values = list(range(left, right+1))

        for i in range(0, len(numbers)):
            divisory = i + 1
            remainder = numbers[i]/divisory
            
            if remainder in values:
                result[i] = True
            else:
                result[i] = False
                
        return result
            
            
res = Solution()
number = [8, 5, 6, 16, 5]
left = 1
right = 3
res.codeWriting(number, left, right)