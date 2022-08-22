from calendar import c


class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
        self.prev = None
        
class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node()
        self.tail = Node()
        currentPage = Node(homepage)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = self.head
        self.insertNode(currentPage)
        # head.next->currentPage->tail

    def insertNode(self, node:Node):
        self.current.next = node
        node.prev = self.current
        self.tail.prev = node
        
    def visit(self, url: str) -> None:
        self.insertNode(Node(url))
        
    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev and self.current.prev.prev:
            self.current = self.current.prev
            steps-=1   
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next and self.current.next.next:
            self.current = self.current.next
            steps-=1
        return self.current.val

class BrowserHistory1:
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pos = 0
        
    def visit(self, url: str) -> None:
        while len(self.stack)-1 != self.pos:
            self.stack.pop()
    
        self.stack.append(url)
        self.pos = len(self.stack)-1
        
    def back(self, steps: int) -> str:
        self.pos -= steps
        
        if self.pos < 0:
            self.pos = 0
        
        return self.stack[self.pos]
        
        
    def forward(self, steps: int) -> str:
        self.pos += steps
        
        if self.pos > len(self.stack)-1:
            self.pos = len(self.stack)-1
        
        return self.stack[self.pos]