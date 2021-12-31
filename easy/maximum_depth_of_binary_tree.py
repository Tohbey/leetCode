from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depthLeft = depthRight = 1

        if root:
            if root.left:
                depthLeft += self.maxDepth(root.left)
            if root.right:
                depthRight += self.maxDepth(root.right)
        else:
            depthLeft = depthRight = 0

        return max(depthLeft, depthRight)