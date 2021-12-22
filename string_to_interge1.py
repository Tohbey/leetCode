class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        number = 0
        new_s = s.lstrip()
        
        if new_s[0:1] == '-':
            sign = -1
            new_s = new_s[1:]
        if new_s[0:1] == '+':
            sign = 1
            new_s = new_s[1:]
            
        for i in range(len(new_s)):
            if new_s[i].isdigit():
                number = number*10 + int(new_s[i])
            else:
                continue
        
        number = number * sign
        
        max, min = 2**31 - 1, -2**31
		 
        if min <= number <= max:
            return number
        else:
            if number > max:
                return max
            else:
                return min


x = "-4578wdejn" 
res = Solution()
ans = res.myAtoi(x)
print(ans)        
        
