from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        memo = ["1"]
        for i in range(1, n):
            num = self._calc(memo[i-1])
            memo.append(num)
        
        return memo[n-1]
    
    def _calc(self, seq: str) -> str:
        result = ""
        for num, group in groupby(seq):
            count = len(list(group))
            result += f"{count}{num}"
        
        return result