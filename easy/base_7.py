class Solution:
    def convertToBase7(self, num: int) -> str:
        remainders = []

        if num<0:
            num, sign = abs(num), "-"

        while(num >= 7):

            remainder = num % 7
            result = num // 7
            num = result
            remainders.append(str(remainder))
        
        if (num <= 7):
            remainders.append(str(num))

        return sign + "".join(remainders[::-1])


res = Solution()
# num = 100
num = -7
result = res.convertToBase7(num)
print(result)