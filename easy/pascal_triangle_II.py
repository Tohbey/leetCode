from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        if rowIndex == 0:
            return result[0];
        
        for i in range(rowIndex+1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            
            result.append(row)
        return result[rowIndex]