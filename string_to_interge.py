class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        number = 0
        # getting rid of leading spaces
        new_s = s.lstrip(" ")
        # checking if signs are affected
        if new_s[0:1] == "-":
            negative = True
            new_s = new_s[1:]
        elif new_s[0:1] == "+":
            new_s = new_s[1:]

        for char in new_s:
		# checking if the charcater is a number :
            if char.isnumeric():
                number = number*10 + int(char)
            else:
                break
			
		# checking if the given number is negative
        if negative :
            number = number * (-1)

        max, min = 2**31 - 1, -2**31
		
		# cheking the range 
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