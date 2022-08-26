from typing import List


class Solution:
    def selectionSort(self, arr: List[int]) -> List[int]:
        for step in range(1, len(arr)):
            key = arr[step]
            j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1

            # Place key at after the element just smaller than it.
                arr[j + 1] = key

        return arr


arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
res = Solution()
result = res.selectionSort(arr)
print(result)
