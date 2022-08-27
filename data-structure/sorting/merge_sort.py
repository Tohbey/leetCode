from typing import List


class Solution:
    def mergeSort(self, arr: List[int]) -> List[int]:
        if len(arr) > 1:
            r = len(arr)//2
            L = arr[:r]
            M = arr[r:]


            self.mergeSort(L)
            self.mergeSort(M)
            i = j = k = 0
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = M[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                arr[k] = M[j]
                j += 1
                k += 1
                
        return arr


arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
res = Solution()
result = res.mergeSort(arr)
print(result)
