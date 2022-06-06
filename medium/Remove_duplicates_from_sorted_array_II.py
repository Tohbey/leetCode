from pip import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        count = 0
        cur = ""
        for i in range(len(nums)):
            if nums[i] != cur:                      # Here comes the new member we haven't met
                nums[idx] = nums[i]                 # Put it to the place "idx"
                count = 1                           # New num has been observed once
                cur = nums[i]                       # Set new num to current current observation candidate 
                idx += 1                            # "idx" jump 1 step, ready to receive next member
            elif nums[i] == cur and count == 1:     # In case the num has appeared once
                nums[idx] = nums[i]
                count += 1
                idx += 1
            elif nums[i] == cur and count == 2:     # Oh, you have been observed more than twice, next one
                continue
        
        return idx
    
    def removeDuplicates2(self, nums: List[int]) -> int:
        max = 2
        hashTable = {}
        for num in nums:
            if num in hashTable:
                if hashTable[num] < max:
                    hashTable[num]+=1
                else:
                    continue        
            else:
                hashTable[num] = 1                
        print(hashTable)
        

res = Solution()
nums = [1,1,1,2,2,3]
res.removeDuplicates2(nums)