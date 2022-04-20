class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	

class Queue:
    def __init__(self):
        self.head = self.rear =None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, val):
        temp = Node(val)

        if self.rear == None:
            self.head = self.rear = temp
            return
        
        self.rear.next = temp
        # updating the rear
        self.rear = temp
    
    def dequeue(self):
        if self.isEmpty():
            return
        
        temp = self.head
        self.head = temp.next

        if self.head is None:
            self.rear = None
    
    def display(self):

        iternode = self.head
        if self.isEmpty():
            print("Queue Underflow")

        else:
            while iternode != None:
                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            return

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
q.dequeue()
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()  
print("Queue Front " + str(q.head.data))
print("Queue Rear " + str(q.rear.data))
q.display()

