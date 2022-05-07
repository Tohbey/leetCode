from pip import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = [0] * len(matrix[0])
        rows, cols = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]) == 0:
                    rows.append(i)
                    cols.append(j)
                    
        for row in rows:
            matrix[row] = zeros
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
        print(matrix)
matrix = [[1,1,1],[1,0,1],[1,1,1]]
res = Solution()
res.setZeroes(matrix)