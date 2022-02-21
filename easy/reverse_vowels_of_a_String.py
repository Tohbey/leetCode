class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A','E','I','O','U','a', 'e', 'i', 'o', 'u']
        left, right = 0, len(s) - 1

        ans = [None] * len(s)

        while left <= right:
            if s[left] not in vowels and s[right]not in vowels:
                ans[left] = s[left]
                ans[right] = s[right]
                left += 1
                right -= 1
            elif s[left] in vowels and s[right] in vowels:
                ans[left] = s[right]
                ans[right] = s[left]
                left += 1
                right -= 1
            elif s[left] in vowels and s[right] not in vowels:
                ans[right] = s[right]
                right -= 1
            elif  s[left] not in vowels and s[right] in vowels:
                ans[left] = s[left]
                left +=1

        return "".join(ans)


res = Solution()
s = 'hello'
print(res.reverseVowels(s))        