class Solution:
    def conversion(self,num:str) -> int:
        value = 0
        for i,j in enumerate(num[::-1]):
            value+=(ord(j)-ord("0"))*10**i
        return value
    
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = self.conversion(num1)
        num2 = self.conversion(num2)

        return str(num1+num2)


res = Solution()
num1 = "11" 
num2 = "123"
print(res.addStrings(num1, num2))