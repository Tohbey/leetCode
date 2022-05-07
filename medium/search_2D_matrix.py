from pip import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == target:
                    return True
        return False
    
    # Binary Search faster
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left, right = 0, len(matrix[i])-1
            while left <= right:
                mid = (left + right)//2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

res = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 33
print(res.searchMatrix(matrix, target))