class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = False
        if x < 0:
            return ans
        
        z = str(x)
        print(z)
        r = len(z) 
        if(len(z) % 2 != 0):
            for i in range(len(z)):
                if z[i] == z[r-1]:
                    ans = True
                elif i == r-1:     
                    break
                else:
                    ans = False
                    break
                    
                r=-1
        if(len(z) % 2 == 0):
            if z == z[::-1]:  
                return True
            
            return False
        return ans

            
    

y = 1000021
res = Solution()
z = res.isPalindrome(y)
print(z)
        