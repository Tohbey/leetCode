from itertools import accumulate


class NumArray:

    def __init__(self, nums: List[int]):
        self.cummlative = [0] + list(accumulate(nums))
        # it creates a list of the sum of the nums list

    def sumRange(self, left: int, right: int) -> int:
        return self.cummlative[right+1] - self.cummlative[left]
