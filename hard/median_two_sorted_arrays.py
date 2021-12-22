from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = float(0)
        nums1.extend(nums2)
        nums1 = sorted(nums1)

        if len(nums1) % 2 == 0:
            middle = len(nums1) // 2

            middleValue = nums1[middle-1]
            middleValue1 = nums1[middle]

            median = (middleValue + middleValue1) / 2
        else:
            n = (len(nums1) //2 ) + 1 
            median = nums1[n - 1]

        return median


num1 = [3, 4]
num2 = [1, 2]

res = Solution()
res.findMedianSortedArrays(num1, num2)
