class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        dict = {}
        for x in range(len(words)):
            if pattern[x] not in dict:
                if  words[x] in dict.values():
                    return False

                dict[pattern[x]] = words[x]
            else:
                if dict[pattern[x]] != words[x]:
                    return False        
        return True

pattern = "abba"
s = "dog cat cat dog"

res = Solution()
print(res.wordPattern(pattern, s))