from os import linesep
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthensis if open < n
        # valid iif open === closed === n
        # only add a closing paranthesis if closed << open
        
        list = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(list))
            
            if openN < n:
                list.append("(")
                backtrack(openN+1, closedN)
                list.pop()
            
            if closedN < openN:
                list.append(")")
                backtrack(openN, closedN+1)
                list.pop()

        backtrack(0,0)
        return res

        

res = Solution()
res.generateParenthesis(1)