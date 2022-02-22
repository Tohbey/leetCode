from pip import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            print(nums1[i])
            if nums1[i] in nums2:
                if nums1[i] not in ans:
                    ans.append(nums1[i])
        
        return ans

res = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(res.intersection(nums1, nums2))