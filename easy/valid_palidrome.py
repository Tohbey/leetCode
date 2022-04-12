class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''.join(i for i in s if i.isalnum()).lower()
        if ans != ans[::-1]:
            return False
        else:
            return True


res = Solution()
s = "A man, a plan, a canal: Panama"
res.isPalindrome(s)