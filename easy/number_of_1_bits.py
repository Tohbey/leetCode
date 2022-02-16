class Solution:
    def hammingWeight(self, n: int) -> int:
        numberofOnes = 0
        
        while n:
            if n & 1 == 1:
                # then last bit was 1
                numberofOnes += 1
            n = n >> 1
        
        return numberofOnes
    
# By "and"-ing with the number "1", we can check if the right most bit is a "1". If it is a 1, then our "and" result should also equal one. If the right most bit is equal to 1, we increment our counter. We then do a logical shift to shift all bits to the right, to get the next right most bit. We do this until our n value is 0 (no more bits left to shift), and return the results.