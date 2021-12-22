class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for x in range(len(s)):
            l, r = x, x
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            l, r = x, x+1
            print(l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l +1) > resLen:
                    res = s[l: r+1]
                    resLen = r -l + 1
                
                l -= 1
                r += 1
        print(res)
        
        return res;

s = "babad"
res = Solution()
res.longestPalindrome(s)