class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_set = set(ransomNote)
        print(rn_set)
        for i in rn_set:
            if ransomNote.count(i) > magazine.count(i):
                return False
        
        return True
        



res = Solution()
ransomNote = "aa" 
magazine = "aab"
print(res.canConstruct(ransomNote, magazine))