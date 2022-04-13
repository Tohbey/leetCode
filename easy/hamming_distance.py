class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s1 = self.returnBinary(x)
        s2 = self.returnBinary(y)
        i,j,ham = 0, 0, 0
        
        while i < len(s1) and j < len(s2):

            if s1[i] != s2[j]:
                ham += 1
            i += 1
            j += 1

        while i < len(s1):
            if s1[i] == "1":
                ham = ham + 1
            i += 1

        while j < len(s2):
            if s2[j] == "1":
                ham = ham + 1
            j += 1

        return ham


    def returnBinary(self, n: int)-> int:
        binary = []
        
        while n >= 2:
            remainder = n % 2
            result = n // 2
            binary.append(str(remainder))
            n = result

        if (n < 2):
            binary.append(str(n))

        return "".join(binary)


res = Solution()
x = 1
y = 3
ham = res.hammingDistance(x, y)
print(ham)