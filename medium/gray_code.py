from pip import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        
        code = self.grayCode(n - 1)
        k = 2 ** (n-1)
        return code + [k + i for i in reversed(code)]