class Solution(object):
    def myPow(self, x, n):
        d = {}

        def multiple(x, n):
            if n == 0:
                return 1

            if n not in d:
                if n % 2 == 1:
                    d[n] = multiple(x, n//2) * multiple(x, n//2) * x
                else:
                    d[n] = multiple(x, n//2) * multiple(x, n//2)
    
            return d[n]
        
        if n < 0:
            return 1 / multiple(x, abs(n))
        else:
            return multiple(x, n)

res = Solution()
x = 2
n = 10
res.myPow(x, n)