# binary tree can have max 2 child , 0 , 1 and 2 childs only.abs

class Node :
    def __init__(self,value): # value = parameter
        self.left = None
        self.right = None
        self.data = value

def preOrder(root): # first then root , left subtree , right subtree
    if(root != None):
        print(root.data , end = " ")
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root): # first left subtree , then root , right subtree
    if(root != None):
        inOrder(root.left)
        print(root.data , end = " ")
        inOrder(root.right)    

def postOrder(root): # first left subtree , then right  subtree ,  root 
    if(root != None):
        postOrder(root.left)
        postOrder(root.right) 
        print(root.data , end = " ")

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right  = Node(4)
root.right.right = Node(8)

print("Preorder:- ")
preOrder(root)

print("\nInorder:- ")
inOrder(root)

print("\nPostorder:- ")
postOrder(root)

# traversal is so easy just focus on root value.