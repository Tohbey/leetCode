class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.next = None


class Queue:
    def __init__(self):
      self.head = None
      self.tail = None

    def peekFront(self):
        if self.isEmptyFront():
            return "EMPTY"
        
        return self.head.dataval
    
    def peekTail(self):
        if self.isEmptyTail():
            return "EMPTY"
        
        return self.tail.dataval      
    
    def enqueue(self,val):
        print("New node", val)
        newNode = Node(val)
        
        if self.isEmptyTail():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self):
        if self.isEmptyFront():
            return "EMPTY"
        else:
            print("Removing ", self.head.dataval)
            temp = self.head
            self.head = self.head.next
            temp.next = None
 

    def isEmptyFront(self):
        if self.head == None:
            return True
        else:
            return False        
        
    def isEmptyTail(self):
        if self.tail == None:
            return True
        else:
            return False        
        
        
    def display(self):
        iternode = self.head
        if self.isEmptyFront():
            print("Stack Underflow")
 
        else: 
            while iternode is not None:
                print(iternode.dataval, "->", end=" ")
                iternode = iternode.next
            return


myQueue = Queue()
print("=============Enqueue Function=============")
myQueue.enqueue(11)
myQueue.enqueue(12)
myQueue.enqueue(13)
myQueue.enqueue(14)
myQueue.enqueue(15)
myQueue.enqueue(16)
myQueue.enqueue(17)
myQueue.enqueue(18)

print("=============Dequeue Function=============")
myQueue.dequeue()
myQueue.dequeue()

print("=============Check head and tail Function=============")
print("Head: ",myQueue.isEmptyFront())
print("Tail: ",myQueue.isEmptyTail())

print("=============Peek Function=============")
print("Head: ",myQueue.peekFront())
print("Tail: ",myQueue.peekTail())

myQueue.display()