from turtle import right


class Solution:
    def simplifyPath(self, path: str) -> str:
        left, right = 0, 1
        ans = ""
        
        while right < len(path):
            if (path[left] == "." and path[right] == '.' 
                or path[left] == "/" and path[right] == "/"):
                ans += path[left]
                left+=2
                right +=2
            elif left == len(path) - 1 and (path[left] == "/" or path[left] == "."):
                break;
            else:
                ans+= path[left]
                left+=1
                right+=1    
                
        print(ans)
        return ans
    
    def simplifyPath1(self, path: str) -> str:
        splitted = path.split('/')
        lst = []
        for i in splitted:
            if i != "":
                lst.append(i)
        stack = []
        for i in lst:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.':
                continue
            else:
                if stack and stack[-1] == '/':
                    stack.append(i)
                else:
                    stack.append('/'+i)
    
        while stack and stack[-1] == '/':
            stack.pop()
    
        return "".join(stack) if len(stack)>0 else '/'
            
        
res = Solution()
path = "/home/."
res.simplifyPath(path)