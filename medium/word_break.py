from ast import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i==len(s): return True
            if i in history and not history[i]: return False
            
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    history[i] = True
                    if dfs(i+len(word)): return True
            history[i] = False
            return False
        
        history = {}
        return dfs(0)
