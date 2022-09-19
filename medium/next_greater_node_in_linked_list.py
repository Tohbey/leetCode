# Definition for singly-linked list.
from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head.next
        stack = []
        stack.append(head)
        
        while(curr is not None):
            if curr.val > stack[len(stack) - 1].val:
                while(len(stack)>0 and stack[len(stack)-1].val < curr.val):
                    poppedNode = stack.pop()
                    poppedNode.val = curr.val
                    
            stack.append(curr)
            curr = curr.next
        
        while len(stack) > 0:
            poppedNode = stack.pop()
            poppedNode.val = 0
            
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
            
        return result