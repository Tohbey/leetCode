# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None or head.next.next == None):
            return head

        odd = odd_curr = head
        even = even_curr = head.next
        curr = head.next.next
        count = 1
        while curr:
            if count % 2 != 0:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            else:
                even_curr.next = curr
                even_curr = even_curr.next
            count = count+1
            curr = curr.next

        even_curr.next = None
        odd_curr.next = even
        return odd
