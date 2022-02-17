class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = self.sum_num(num)
        
        return num

    def sum_num(self, num):
        sum = 0
        while num//10 > 0:
            sum += num % 10
            num = num//10

        sum += num

        return sum


res = Solution()
num = 38

print(res.addDigits(num))
