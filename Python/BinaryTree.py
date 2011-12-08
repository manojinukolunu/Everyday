class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def printData(self):
        print self.data

        

class BTree:
    def __init__(self):
        root=Node(1)
        node1=Node(2)
        node2=Node(3)
        node1.printData()
    def insertNode(self,Node):
        if Node.data<root.data:
            insertNode(root.left)
        elif Node.data>root.data:
            insertNode(root.right)
        
    


      
