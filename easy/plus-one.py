from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # get the lat item add one check if its equals 9 insert 0 to the positionof one and add 1 to the next position  , else just add 1 and return 
        if digits[-1] ==9:
            for i in range(len(digits)-1,-1,-1):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    return digits
            res=[1]
            res.extend(digits)
            return res
        else:
            digits[-1]+=1
            return digits