from typing import Optional

from pip import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def inorder(root, curr_path):
            if root and not root.left and not root.right:
                path = "->".join(curr_path + [str(root.val)])
                paths.append(path)
                return
            
            if not root:
                return
            
            curr_path.append(str(root.val))
            inorder(root.left, curr_path)
            inorder(root.right, curr_path)
            curr_path.pop()
            
        inorder(root, [])
        return paths

