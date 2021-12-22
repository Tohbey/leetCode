class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        roman = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
                 "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5,
                 "IV": 4, "I": 1}

        while num >= 1:
            for key in roman.keys():
                if num - roman[key] >= 0:
                    ans += key
                    num -= roman[key]
                    break
        print(ans)
        return ans


res = Solution()
res.intToRoman(54)
