from pip import List


class Solution:
    def bubbleSort(self, arr:List[int]) -> List[int]:
        n = len(arr)
 
        # Traverse through all array elements
        for i in range(n):
    
            # Last i elements are already in place
            for j in range(0, n-i-1):
    
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

arr = [64, 34, 25, 12, 22, 11, 90]
res = Solution()
result = res.bubbleSort(arr)
print(result)