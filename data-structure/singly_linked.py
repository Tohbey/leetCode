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

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return

        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval

        laste.nextval = NewNode

    def Inbetween(self, middle_node:Node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def RemoveNode(self, RemoveKey):
        Headval = self.headval

        if(Headval is not None):
            if(Headval.dataval == RemoveKey):
                self.headval = Headval.nextval
                Headval = None
                return

        while (Headval is not None):
            if Headval.dataval == RemoveKey:
                break
            prev = Headval
            Headval = Headval.nextval
        
        if(Headval == None):
            return
        
        prev.nextval = Headval.nextval
        Headval = None


list = SLinkedList()
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

list.headval.nextval = e2
e2.nextval = e3
list.AtBegining("Sunday")
list.AtEnd("Thursday")
list.listprint()
