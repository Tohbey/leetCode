class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman = {
            "I": 1,
            "V": 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        if(len(s) == 1):
            return roman[s]
        
        for i in range(len(s)):            
            if s[i] == "I":
                if i+1 != len(s):
                    if s[i+1] == 'V' or s[i+1] == 'X':
                        ans-=1
                    else:
                        ans+=1
                else:
                    ans+= 1
            elif s[i] == 'X':
                if i+1 != len(s):
                    if s[i+1] == 'L' or s[i+1] == 'C':
                        ans-=roman[s[i]]
                    else:
                        ans+=roman[s[i]]
                else:
                    ans+=roman[s[i]]
            elif s[i] == 'C':
                if i+1 != len(s):
                    if s[i+1] == 'D' or s[i+1] == 'M':
                        ans-=roman[s[i]]
                    else:
                        ans+=roman[s[i]]
                else:
                    ans+=roman[s[i]]
            else:
                ans+=roman[s[i]]
            
        print(ans)    

        
s= "LVIII"
res = Solution()
res.romanToInt(s)