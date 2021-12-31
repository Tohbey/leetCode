# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        
        current = head.next 
        prev = head 
        
        while(current):
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else: 
                prev = current
                prev.next = current.next
        
        return head