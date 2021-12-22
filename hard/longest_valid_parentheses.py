class Solution:
    #     def longestValidParentheses(self, s: str) -> int:
#         closed = {'(': ')'}
#         stack = ['']
#         ans = 0
#         if len(s) == 0:
#             return ans
        
#         for i in range(len(s)):
#             if i+1 < len(s):
#                 if s[i] in closed and s[i+1] == closed[s[i]]:
#                     ans+=2
#             else:
#                 return ans
            
    def longestValidParentheses(self, s: str) -> int:
            stack = []
            count = 0

            stack.append(-1)

            for i in range(len(s)):
                if s[i]=='(':
                    stack.append(i)
                else:
                    stack.pop()
                    if not stack:
                        stack.append(i)
                    else:
                        count = max(count, i-stack[-1])

            return count