from pip import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
                nums2.remove(nums1[i])

        return ans


res = Solution()
nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
res.intersect(nums1, nums2)