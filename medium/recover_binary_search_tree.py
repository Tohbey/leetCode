# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.first = None
        self.prev = TreeNode(-1000000000000)
        self.mid = None
        self.last = None
    
    def inorder(self,root):
        if root == None:
            return
        
        self.inorder(root.left)
        
        if self.prev != None and root.val < self.prev.val :
            if self.first == None:
                self.first = self.prev
                self.mid = root
            else:
                self.last = root
        
        self.prev = root
        
        self.inorder(root.right)
        
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        self.inorder(root)
        if self.first and self.last :
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.mid:
            self.first.val, self.mid.val = self.mid.val, self.first.val
        
        