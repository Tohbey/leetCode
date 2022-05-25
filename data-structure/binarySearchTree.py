import collections
from typing import Collection


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    #Insert a node     
    def insert(node, value):
        if node is None:
            return Node(value)
        
        #recursive function because we are comparing from the top of the node
        if value < node.value:
            node.left = Node.insert(node.left, value)
        else:
            node.right = Node.insert(node.right, value)
        
        return node
    

    def preorder(node):
        if node is None:
            return 
        
        print(str(node.value) + '->', end=' ')
        Node.preorder(node.left)
        Node.preorder(node.right)
        
    
    def inorder(node):
        if node is None:
            return 

        Node.inorder(node.left)
        print(str(node.value) + '->', end=' ')
        Node.inorder(node.right)
    
    def postorder(node):
        if node is None:
            return 

        Node.postorder(node.left)
        Node.postorder(node.right)
        print(str(node.value) + '->', end=' ')

    def searching(root, value):
        if root is None:
            return root
        
        if value < root.value:
            if root.left is None:
                return str(value) + " not found"
            return Node.searching(root.left, value)
        elif value > root.value:
            if root.right is None:
                return str(value) + " not found"
            return Node.searching(root.right, value)
        else:
            print(str(root.value) + ' is found')

    def find_min(node):        
        while node.left is None:
            return node.value
            
        return Node.find_min(node.left)
    
    def find_max(node):
        if node.right is None:
            return node.value

        return Node.find_max(node.right)
    
    def deleteNode(root, value):
        if root is None:
            return root
        
        if value < root.value:
            root.left = Node.deleteNode(root.left, value)
        elif value > root.value:
            root.right = Node.deleteNode(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            minValue = Node.find_min(root.right)
            
            root.value = minValue
            root.right = Node.deleteNode(root.right, minValue)
            
            return root
    
    def levelOrder(node):
        ans = []
        if node is None:
            return ans
        
        queue = collections.deque()
        queue.append(node)
        
        while queue:
            currSize = len(queue)
            currList = []
            
            while currSize > 0:
                
                currNode = queue.popleft()
                currList.append(currNode.value)
                currSize -=1
                
                if currNode.left is not None:
                    queue.append(currNode.left)
                if currNode.right is not None:
                    queue.append(currNode.right)
                    
            ans.append(currList) 
        
        print(ans)
        return ans

    def minValueNode(node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current
        
root = 6
res = Node(root)
res.insert(8)
res.insert(3)
res.insert(1)
res.insert(6)
res.insert(7)
res.insert(10)
res.insert(14)
res.insert(4)

print(res.searching(4))

res.deleteNode(8)

print(res.find_min())
print(res.find_max())
res.inorder()
print('\n')
res.postorder()
print('\n')
res.preorder()
print('\n')
res.levelOrder()