class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == abs(1):
            return True

        else:
            if n % 4 == 0:
                k = n/4

                return self.isPowerOfFour(k)
            else:
                return False