class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def push(self, Newval):
        NewNode = Node(Newval)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode

        self.head = NewNode

    def listprint(self, node: Node):
        while (node is not None):
            print(node.data)
            node = node.next

    def insert(self, prev_node: Node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
           NewNode.prev = None
           self.head = NewNode
           return
        last = self.head
        while (last.next is not None):
          last = last.next
        last.next = NewNode
        NewNode.prev = last
        return


dllist = DLinkedList()
dllist.push(12)
dllist.append(9)
dllist.push(8)
dllist.push(62)
dllist.append(45)
dllist.listprint(dllist.head)