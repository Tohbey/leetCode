from collections import Counter

from pip import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic=Counter(nums)
        print(dic)
        for i in dic.keys():
            if(dic[i]==1):
                return i
            

res = Solution()
nums=[2,2,3,2]
res.singleNumber(nums)