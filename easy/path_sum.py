# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isSum = False
    def hasPathSum(self, root, targetSum):
        
        def dfs(root,targetSum):
            if root:
                targetSum -= root.val
                if targetSum == 0 and root.left is None and root.right is None:
                    self.isSum = True
                left = dfs(root.left,targetSum)
                right = dfs(root.right,targetSum)
            return self.isSum
        
        return dfs(root,targetSum)
        