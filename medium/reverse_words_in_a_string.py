class Solution:
    def reverseWords(self, s: str) -> str:
        a=list(s.split())
        s=""
        for i in a:
            if i!="":
                s=(i+" ")+s
        return s[:-1]
        
s = "blue is sky the"
res = Solution()
ans = res.reverseWords(s)
print(ans)