from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leftleaves(root,False)
        
    def leftleaves(self,root,left):
        if(root==None):
            return 0

        elif(root.left==None and root.right==None):
            if(left==True):
                return root.val
            if(left==False):
                return 0  
        
        else:
            return self.leftleaves(root.left,True) + self.leftleaves(root.right,False)