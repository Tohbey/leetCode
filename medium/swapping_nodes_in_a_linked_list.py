# Definition for singly-linked list.
from multiprocessing import dummy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = dummy = ListNode(0, head)
        c = 0
        curr = curr.next
        
        while curr:
            c+=1
            curr=curr.next
            
        endK = c-k+1
        curr = head
        c = 1
        curr = dummy
        
        while curr:
            if c == k:
                prestart = curr
            if c == k+1:
                start = curr
            if c == endK:
                preend = curr 
            if c == endK+1:
                    end = curr 
                
            c+=1
            curr = curr.next
        
        if start == end:
            return head
        
        prestart.next,preend.next = end, start
        start.next, end.next = end.next, start.next
        
        return dummy.next