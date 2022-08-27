from typing import List


class Solution:
    def quickSort(self, arr: List[int]) -> List[int]:

        less = []
        equal = []
        greater = []

        if len(arr) > 1:
            pivot = arr[0]
            for x in arr:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return self.quickSort(less)+equal+self.quickSort(greater)
        else:
            return arr


arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
res = Solution()
result = res.quickSort(arr)
print(result)
