class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        if n == abs(1):
            return True

        else:
            if n % 2 == 0:
                k = n/2

                return self.isPowerOfTwo(k)
            else:
                return False
