class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() == True or word.isupper() == True:
            return True
        if word[0].isupper() == True and word[1:len(word)].islower() == True:
            return True
        else:
            return False