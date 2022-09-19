class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None
        

class MyCircularDeque:
    
    def __init__(self, k: int):
        head_node = Node(0)
        self.len = 0
        self.limit = k
        cur = head_node
        
        for i in range(1, k):
            cur.next = Node(i)
            cur.next.prev = cur
            
            cur = cur.next
            
        cur.next = head_node
        head_node.prev = cur
        
        self.head = head_node.prev
        self.tail = head_node

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.head.value = value
        self.head = self.head.prev
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if (self.isFull()):
            return False 
                       
        self.tail.value = value
        self.tail = self.tail.next
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = self.head.next
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.tail = self.tail.prev
        self.len -= 1
        return True

    def getFront(self) -> int:
        if(self.isEmpty()):
            return -1
        
        return self.head.next.value        

    def getRear(self) -> int:
        if(self.isEmpty()):
            return -1
        
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.limit