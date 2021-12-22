from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if len(strs) == 0  : 
            return ''
        
        short = min(strs,key = len) 
        print(short)
        
        if len(strs) == 1: 
            return strs[0]
        
        
        for i in range(0,len(short)): 
            for j in strs : 
                if short[:i+1] != j[:i+1] : 
                    if i-1 > -1 :
                        return short[:i]
                    else :
                        return ''
                else : 
                    pass
        return short
        
            
names = ["flower","flow","flight"]
res = Solution()
print(res.longestCommonPrefix(names))