from pip import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows, cols = (n,n)
        matrix = [[0]* cols]*rows
       

n = 3
res = Solution()
res.generateMatrix(n)