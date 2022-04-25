from pip import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0 , len(matrix[0])
        top, bottom = 0, len(matrix) 
        result = []

        while left < right and top < bottom:
            # get every i the top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top +=1

            # get every i in right col
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in bottom row
            for i in range(right - 1, left -1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1

            #get every i in the left collections
            for i in range(bottom -1, top -1, -1):
                result.append(matrix[i][left])
            
            left += 1
        return result

res = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
res.spiralOrder(matrix)