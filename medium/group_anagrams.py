from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        if len(strs) == 1:
            return result.append(strs)    


res = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
res.groupAnagrams(strs)