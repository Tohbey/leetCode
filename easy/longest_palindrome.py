class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for l in s:
            if l not in d.keys():
                d[l]=1
            else:
                d[l]+=1
        
        res=0 
        odd=False
        for value in d.values():
            if value%2==0:
                res+=value
            else:
                odd=True
                res+=(value-1)
        if odd:
            return res+1
        else:
            return res