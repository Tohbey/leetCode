# Definition for a binary tree node.
from typing import Optional
from pip import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        
        root.right = self.buildTree(inorder[mid+1:],postorder[mid:-1])
        root.left = self.buildTree(inorder[:mid],postorder[:mid])        
        return root
    
    
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
res = Solution()
res.buildTree(inorder, postorder)