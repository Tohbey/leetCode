class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        minValue = 64
        result = 0
        for i in range(0, len(columnTitle)):
            result = result*26 + (ord(columnTitle[i]) - minValue)
            
            print(result)
        
        return result
result = Solution()
columnTitle = 'AB'

result.titleToNumber(columnTitle)