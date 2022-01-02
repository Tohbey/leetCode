# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums)-1
        
        def helper(l, r): 
            if l > r:
                return None
            
            mid = (l + r)//2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid-1)
            root.right = helper(mid+1, r)
            
            return root
        
        return helper(left, right)