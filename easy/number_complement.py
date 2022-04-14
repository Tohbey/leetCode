class Solution:
    def findComplement(self, num: int) -> int:
        new = str(bin(num))
        str1 = ''
        new = new.replace('0b', '')
        for i in new:
            if i == '1':
                str1 += '0'
            else:
                str1 += '1'
        ans = 0
        count = 0

        for i in range(len(str1)-1, -1, -1):
            if(str1[i] == '1'):
                ans += (2**count)*1
                count += 1
            else:
                count += 1
        
        return ans



res =  Solution()
num = 5
ans = res.findComplement(num)
print(ans)