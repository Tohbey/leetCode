from math import remainder


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if numerator/denominator < 0:
            res += "-"
        if numerator % denominator == 0:
            return str(numerator/denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator/denominator)
        res += "."
        numerator %= denominator
        i = len(res)
        table = {}
        while numerator != 0:
            if numerator not in table.keys():
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i]+"("+res[i:]+")"
                return res
            numerator = numerator*10
            res += str(numerator/denominator)
            numerator %= denominator
            i += 1
        return res

        


res = Solution()
res.fractionToDecimal(4, 333)
