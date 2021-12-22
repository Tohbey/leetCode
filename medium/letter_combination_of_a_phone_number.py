from typing import List


class Solution:
    def letterCombinations(self, digits: str):
        result = []
        hashmap = {
            "2": ["a","b", "c"], 
            "3": ["d", "e", "f"], 
            "4": ["g", "h", "i"], 
            "5": ["j", "k", "l"], 
            "6": ["m", "n", "o"], 
            "7": ["p", "q", "r", "s"], 
            "8": ["t", "u", "v"], 
            "9": ["w", "x", "y", "z"]
        }
        
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return hashmap[digits[0]]
        
        def backtrack (i, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            
            for c in hashmap[digits[i]]:
                backtrack(i+1, curStr+c) 
    
        if len(digits) > 1:
            backtrack(0, "")
        
        print(result)
        return result

digits = "23"
res = Solution()
res.letterCombinations(digits)            
