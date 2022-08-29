class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None


class SLinkedList:
    def __init__(self):
      self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
          print(printval.dataval)
          printval = printval.nextval

    def AtBegining(self, newData):
        NewNode = Node(newData)
        # setting the former head val to the next val of the new header
        NewNode.nextval = self.headval
        # settting the new header as the headval
        self.headval = NewNode

    def AtEnd(self, newData):
        NewNode = Node(newData)
        # checking if the head node is empty then setting the new node to the headNode
        if self.headval is None:
            self.headval = NewNode
            return
        
        #loop through the array to get the end node and set the nextval to a new node
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        
        laste.nextval = NewNode
    
    def Inbetween(self, middle_node, newData):
        if middle_node is None:
            print("The mentioned node is absence")
            return
        
        NewNode = Node(newData)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    
    def RemoveNode(self, RemoveKey):
        HeadVal = self.headval

        if(HeadVal is not None):
            if(HeadVal.dataval == RemoveKey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
            
            while(HeadVal is not None):
                if(HeadVal.dataval == RemoveKey):
                    break
                prev = HeadVal
                HeadVal = HeadVal.nextval
            
            if(HeadVal == None):
                return
            
            prev.nextval = HeadVal.nextval
            HeadVal = None



list1 = SLinkedList()
# assigning the header
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list1.Inbetween(list1.headval.nextval, "Fri")
list1.AtBegining("Sun")
list1.RemoveNode("Tue")
list1.AtEnd("Thu")
list1.listprint()
