from pip import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        max_num = 0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    max_num += 1
                    s.remove(s[j])
                    break  
        return max_num