from pip import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        i = 1
        while i <= n:
            if i%3 == 0 and i%5 == 0:
                result.append("FizzBuzz")
            elif i%5 == 0:
                result.append("Buzz")
            elif i%3 == 0:
                result.append("Fizz")
            else:
                result.append(str(i))
            
            i = i + 1

        print(result)

res = Solution()
n = 15
res.fizzBuzz(n)
