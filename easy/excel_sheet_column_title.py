class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        minValue = 64
        str1 = ''
        while columnNumber > 0: 
            chr1 = columnNumber % 26
            print(chr1)
            if chr1 == 0: 
                chr1 = 26
                columnNumber -= 1
            str1 = chr(minValue+chr1) + str1
            columnNumber = columnNumber //26
        
        return str1
    
res= Solution()
columnNumber = 28

print(res.convertToTitle(columnNumber))