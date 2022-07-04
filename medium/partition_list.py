# Definition for singly-linked list.
import re
from turtle import right
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftList = ListNode()
        rightList = ListNode()
        ltail, rtail = leftList, rightList
        
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
                
            head = head.next
        
        ltail.next = rightList.next
        rtail.next = None
        
        return leftList.next