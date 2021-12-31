from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else: 
                digits[i] +=1
                return digits
        
        digits = [1]+ digits
        return digits

digits = [1,2,9]
res = Solution()
print(res.plusOne(digits))   