class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None
        self.prev = None
        
        
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmptyHead(self):
        if self.head is None:
            return True
        else: 
            return False
        
    def isEmptyTail(self):
        if self.tail is None:
            return True
        else: 
            return False
        
    
    def append(self, val):
        print("New Value add: ", val)
        newNode = Node(val)
        
        if self.isEmptyHead():
            self.tail = self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            
    def appendRight(self, val):
        print("New Value add: ", val)
        newNode = Node(val)
        
        if self.isEmptyTail():
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            
    def pop(self):
        if self.isEmptyTail():
            return "Empty"
        else:
            print("Removed: ", self.tail.dataval)
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
        
    def popLeft(self):
        if self.isEmptyHead():
            return "Empty"
        else:
            print("Removed: ", self.head.dataval)
            temp = self.head
            self.head = temp.next
            self.head.prev = None
    
    def getHead(self):
        if self.isEmptyHead():
            return "Empty"
        else:
            return self.head.dataval
        
    def getTail(self):
        if self.isEmptyTail():
            return "Empty"
        else:
            return self.tail.dataval
        
    def display(self):
        iternode = self.head
        if self.isEmptyHead():
            print("Stack Underflow")
 
        else: 
            while iternode is not None:
                print(iternode.dataval, "<-->", end=" ")
                iternode = iternode.next
            return

myDeque = Deque()
print("=============Append Function=============")
myDeque.append(11)
myDeque.append(12)
myDeque.append(13)
myDeque.append(14)
myDeque.append(15)
myDeque.display()

print("=============Append Right Function=============")
myDeque.appendRight(16)
myDeque.appendRight(17)
myDeque.appendRight(18)
myDeque.appendRight(19)
myDeque.appendRight(20)

print("=============Display Function=============")
myDeque.display()

print("=============Tail Function=============")
print(myDeque.getTail())
print("=============Head Function=============")
print(myDeque.getHead())

print("=============Remove Tail Function=============")
myDeque.pop()
print("=============Remove Head Function=============")
myDeque.popLeft()

print("=============Get Tail Function=============")
print(myDeque.getTail())
print("=============Get Head Function=============")
print(myDeque.getHead())

myDeque.display()