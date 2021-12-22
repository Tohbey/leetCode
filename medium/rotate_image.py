from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1 
        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                
                #save the topleft
                topLeft = matrix[top][l+i]
                
                #move the bottom left into the top left
                matrix[top][l+i] = matrix[bottom-i][l]
                
                #move the bottom right into the bottom left 
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                #move the top right into the bottom right 
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # move top left into top right
                matrix[top+i][r] = topLeft
                
                r-=1
                l+=1