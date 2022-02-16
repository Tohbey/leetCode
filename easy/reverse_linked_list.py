# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # solution 1
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev


    # solution 2 
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList1(head.next)
            head.next.next = head
        
        head.next = None
        
        return newHead

        
