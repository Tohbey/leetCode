# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        level = []
        res = 1
        while q and root:
            for node in q:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            q = level
            res += len(level)
            level = []
        return res