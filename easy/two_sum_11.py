from typing import List



class Solution:
    def twoSum(self, numbers: List[int], target:int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while(left< right):
            sum = numbers[left] + numbers[right]
            print(sum)
            if sum > target:
                right-=1
            elif sum < target:
                left+=1
            else:
                return [left+1, right+1]
        return []


res = Solution()
numbers = [1, 3, 4, 5, 7, 10, 11]
target = 9

res.twoSum(numbers, target)
