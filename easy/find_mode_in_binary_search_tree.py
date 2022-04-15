from argparse import OPTIONAL

from pip import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def findMode(self, root: OPTIONAL[TreeNode]) -> List[int]:
        modes = []
        res = self.inorder(root, [])
        

    def inorder(self, root, lst):
        if root:
            self.inorder(root.left, lst)
            lst.append(root.val)
            self.inorder(root.right, lst)

        return lst