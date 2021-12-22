class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 :  
            return False
        closed = {'(': ')', '{': '}', '[': ']'}
        close_ = {')',']','}'}
        open_ = {'(', '[', '{'}
        stack = ['']
        
        for bracket in s:
            if bracket in open_:
                stack.append(closed[bracket])
            elif bracket != stack.pop():
                return False
        
        return True if len(stack)-1 == 0 else False
    

s = "[]"
res = Solution()
print(res.isValid(s))
