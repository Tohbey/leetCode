class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def rec(i):
            if i in cache:
                return cache[i]
            if i <= i: return i
            cache[i] = rec(i-1) + rec(i-2)

            return cache[i]

        return rec(n)

res = Solution()
ans = res.fib(2)
print(ans)