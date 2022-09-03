class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.next = None


class Stack:
    def __init__(self):
      self.head = None

    def peek(self):
        if self.isEmpty():
            return "EMPTY"
        
        return self.head.dataval      
    
    def push(self, val):
        print("New node", val)
        if self.isEmpty():
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.isEmpty():
            return "EMPTY"
        else:
            print("Removing ", self.head.dataval)
            temp = self.head
            self.head = self.head.next
            temp.next = None
 
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False        
        
        
    def display(self):
        iternode = self.head
        if self.isEmpty():
            print("Stack Underflow")
 
        else: 
            while iternode is not None:
                print(iternode.dataval, "->", end=" ")
                iternode = iternode.next
            return


stack = Stack()

print("=============Push Function=============")
stack.push(11)
stack.push(12)
stack.push(13)
stack.push(14)
stack.push(15)
stack.push(16)
stack.push(17)

print("=============Empty Function=============")
print(stack.isEmpty())

print("=============Peek Function=============")
# returns the header
print(stack.peek())

print("=============Pop Function=============") 
# remove the header
stack.pop()
print("=============Display Function=============")
stack.display()