from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return False;
        
        def dfs(n, m):
            if not n and not m:
                return True;
            
            if n and m and n.val == m.val:
                return dfs(n.left, m.right) and dfs(n.right, m.left);
        
        
        return dfs(root, root)