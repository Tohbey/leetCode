class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        for i in range(len(t)):
            if j == len(s):
                return True

            print(s[j], t[i])
            if s[j] == t[i]:
                j += 1

        if j == len(s):
            return True

        return False


s = "acb"
t = "ahbgdc"

res = Solution()
print(res.isSubsequence(s, t))
