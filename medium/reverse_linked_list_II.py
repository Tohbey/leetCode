from multiprocessing import dummy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev = dummy
        cur = head
        
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
            
        # Now cur = "left", leftPrev = "node before left"
        # revserse from left to right 
        prev = None
        for i in range(right - left + 1):
            tempNext = cur.next
            cur.next = prev
            prev, cur = cur, tempNext
            
        # curr = "right.next node"
        leftPrev.next.next = cur
        
        # prev = "right node"
        leftPrev.next = prev
        
        return dummy.next