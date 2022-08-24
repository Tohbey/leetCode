# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        resultList = []
        result = 0
        while current:
            resultList.append(current.val)
            tmp = current.next
            current = tmp
        
        for i in range(0, len(resultList)):
            result+=resultList[i]*2**(len(resultList)-i-1)            
    
        return result
            
        
        