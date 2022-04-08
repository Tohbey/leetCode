from pip import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        binary = []

        for i in range(n+1):
            binary.append(str(self.returnBinary(i)))
            output.append(binary[i].count('1'))
        
        print(output)
        return output

    def returnBinary(self, n: int)-> int:
        binary = []
        
        while n >= 2:
            remainder = n % 2
            result = n // 2
            binary.append(str(remainder))
            n = result

        if (n < 2):
            binary.append(str(n))

        return "".join(binary[::-1])


res =Solution()
n = 5
res.countBits(n)