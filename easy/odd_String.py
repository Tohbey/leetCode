class Solution:
    def solve(self, m, s):
        # fill this function
        result = [] * len(s)
        sum = 0
        for i in range(0, len(s)):
            sumArray = 1
            for j in range(0, len(s[i])):
                asciiValue = ord(s[i][j])**m
                print(asciiValue)
                sumArray = sumArray * asciiValue
            
            sum+=sumArray            
        if sum%2 == 0:
            return "Even"
        else:
            return "ODD"
        
    def solve2(self, m, s):
        isStringEven = []*len(s)
        for i in range(0, len(s)):
            isEvenPresent = False
            for j in range(0, len(s[i])):
                tempVal = ord(s[i][j])
                if(tempVal%2 == 0):
                    isEvenPresent = True
            
            isStringEven.append(isEvenPresent)

        oddCount = 0
        for i in range(0, len(s)):
            if isStringEven[i] == False:
                oddCount+=1
        
        if oddCount%2 != 0:
            return "ODD"
        else:
            return "EVEN" 
        
res = Solution()
s= ["abc","abcd"]
m = 2
print(res.solve(m,s))