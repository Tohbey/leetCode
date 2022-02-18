from pip import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        replacementIndex = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[replacementIndex] = num
                replacementIndex += 1

        
        endOfNonZero = replacementIndex


        for index in range(endOfNonZero, len(nums)):
            nums[index] = 0
        return nums

    # def moveZeroes2(self, nums: List[int]) -> None:

    #     for i in range(len(nums)):
    #         if nums[i] == 0 and (i+1) < len(nums)-1:
    #             temp = nums[i]
    #             nums[i] = nums[i+1]
    #             nums[i+1] = temp
    #             print(i,temp)
    #         elif nums[i] == 0 and nums[i+1] == 0 and (i+2) < len(nums)-1:
    #             temp = nums[i]
    #             nums[i] = nums[i+2]
    #             nums[i+2] = temp
        
    #     return nums



nums = [0, 1, 0, 3, 12]
res = Solution()

print(res.moveZeroes2(nums))
