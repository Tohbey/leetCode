from pip import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[len(matrix)-1][len(matrix)-1]
        print(left, right)
            
        while left < right:
            mid = left + (right - left)//2
            print(mid)
            
            total = 0
            
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] <= mid:
                        total+=1 # count the number of vals <= mid
            
            if total < k:
                left = mid + 1
            else:
                right = mid
        return left
    
res = Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(res.kthSmallest(matrix,k))