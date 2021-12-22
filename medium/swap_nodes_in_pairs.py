class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode):
        if head is None:
            return None
        
        prev = None
        current = head
        nex = current.next
        
        if nex is None:
            return head
        else:
            head = head.next
        
        while current is not None and nex is not None:
            current.next = nex.next
            nex.next = current
            
            if prev is None:
                prev = current
            else:
                prev.next = nex
                prev = current
            
            if current is not None:
                current = current.next
                if current is not None:
                    nex = current.next
            
        return head