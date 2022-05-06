from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        lenght, tail = 1, head
        
        while tail.next:
            tail = tail.next
            lenght+=1
            
        
        k = k % lenght
        if k == 0:
            return head
        
        
        cur = head
        for i in range(lenght- k - 1):
            cur = cur.next
            
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead