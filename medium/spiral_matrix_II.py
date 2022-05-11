from pip import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [['*' for _ in range(n)] for _ in range(n)]
        row, col = 0, 0
        num = 1
        while num <= n*n:
            while col < n and matrix[row][col] == '*':
                matrix[row][col] = num
                num += 1
                col += 1
            col -= 1
            row += 1
            
            while row < n and matrix[row][col] == '*':
                matrix[row][col] = num
                num += 1
                row += 1
            row -= 1
            col -= 1
            
            while col >= 0 and matrix[row][col] == '*':
                print("Left : ",num)
                matrix[row][col] = num
                num += 1
                col -= 1
            col += 1
            row -= 1
            
            while row >= 0 and matrix[row][col] == '*':
                matrix[row][col] = num
                num += 1
                row -= 1
            row += 1
            col += 1
        return matrix
       

n = 3
res = Solution()
res.generateMatrix(n)