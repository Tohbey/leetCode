from math import remainder


class Solution:
    def toHex(self, num: int) -> str:
        hexadecimal = 16
        hexadecimalLibrary = {10: 'a',11: 'b',12: 'c',13: 'd',14: 'e',15: 'f'}
        remainders = []

        if num<0:
            num += 2**32

        while(num >= hexadecimal):

            remainder = num % hexadecimal
            result = num // hexadecimal
            num = result
            if remainder in hexadecimalLibrary:
                remainders.append(hexadecimalLibrary[remainder])
            else:
                remainders.append(str(remainder))
        
        if (num <= hexadecimal):
            if num in hexadecimalLibrary:
                remainders.append(hexadecimalLibrary[num])
            else:
                remainders.append(str(num))

        return "".join(remainders[::-1])
            



res = Solution()
num = 16
res.toHex(num)
