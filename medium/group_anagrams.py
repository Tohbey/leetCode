from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #mapping the charcount to the list of anagrams
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            result[tuple(count)].append(s)

        return result.values()
    
res = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
res.groupAnagrams(strs)