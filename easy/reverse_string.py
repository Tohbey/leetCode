from pip import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, sLenght =0, len(s) - 1
        while i < sLenght:
            temp = s[i]
            temp1 = s[sLenght] 
            s[sLenght] = temp
            s[i] = temp1

            i+=1
            sLenght -= 1

        print(s)

res = Solution()
# s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
res.reverseString(s)