class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum = self.factorial(n)    
        print(sum)    
        count = 0
        sum = str(sum)
        for i in range(len(sum) -1, -1, -1):
            if sum[i] == "0":
                count +=1
            else:
                break
                
        print(count)
        return count
    
    def trailingZeroes1(self, n):
        x   = 5
        res = 0
        while x <= n:
            res += n//x
            x   *= 5
        return res
    
    def factorial(self,x:int) -> int:
        if x == 1:
            return 1
        else:
            return (x * self.factorial(x-1))

res = Solution()
n = 7
res.trailingZeroes(n)