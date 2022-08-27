from random import randint
from typing import List


class Solution:
    def countingSort(self, arr: List[int]) -> List[int]:
        counter = {}
        for i in range(0, len(arr)):
            if arr[i] in counter:
                counter[arr[i]]+=1
            else:
                counter[arr[i]] = 1
                
        for i in counter:
            print(counter.get(i))


arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
res = Solution()
result = res.countingSort(arr)
print(result)
