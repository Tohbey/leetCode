import collections
import queue
from typing import Optional

from pip import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        idx = 0       
        q = collections.deque([root])
        while q:
            q_length = len(q)
            level = []
            for i in range (q_length):
                target_node = q.popleft()
                if target_node:
                    level.append(target_node.val)
                    q.append(target_node.left)
                    q.append(target_node.right)
                    
            if level:
                if idx % 2 == 0:
                    result.append(level)
                else: 
                    result.append(level[::-1])
                idx += 1
        return result