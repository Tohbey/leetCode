class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == abs(1):
            return True

        else:
            if n % 3 == 0:
                k = n/3

                return self.isPowerOfThree(k)
            else:
                return False