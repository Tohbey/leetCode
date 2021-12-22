class Node:
        def __init__(self, val=None):
            self.val = val
            self.nextval = None

class Solution:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
          print(printval.val)
          printval = printval.nextval

    def AtBegining(self, newData):
        NewNode = Node(newData)
        # setting the former head val to the next val of the new header
        NewNode.nextval = self.headval
        # settting the new header as the headval
        self.headval = NewNode

    def addTwoNumbers(self, l1: Node, l2: Node):
        prev:Node = None
        carry = 0
        temp = None
        while(l1 is not None or l2 is not None):
            fdata = 0 if l1 is None else l1.val
            sdata = 0 if l2 is None else l2.val
            sum = carry + fdata + sdata

            carry = 1 if sum >= 10 else 0

            sum = sum if sum < 10 else sum % 10

            temp = Node(sum)
            if self.headval is None:
                self.headval  = temp
            
            else:
                prev.nextval = temp

            prev = temp
            if l1 is not None:
                l1 = l1.nextval
            
            if l2 is not None:
                l2 = l2.nextval

        if carry > 0:
            temp.nextval = Node(carry)
        
        return list

first = Solution()
second = Solution()

# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9] 
l2 = [9,9,9,9]

for i in l1:
    first.AtBegining(i)


for x in l2:
    second.AtBegining(x)

first.listprint()
second.listprint()

res = Solution()
res.addTwoNumbers(first.headval, second.headval)
res.listprint()