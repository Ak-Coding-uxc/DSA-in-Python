class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
    
def insert(root , value):
    if(root == None):
        return Node(value)
    if(root.data == value):
        return root
    if(root.data > value):
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data , end = " ")
        inOrder(root.right)

def search(root , value):
    if(root == None):
        print("\nNot found any value")
        return        
    if(root.data == value):
        print("\nFound value")
        return
    if(root.data > value):
        search(root.left,value)
    else:
        search(root.right,value)

root = None
root = insert(root , 20)
root = insert(root, 50)
root = insert(root, 90)
root = insert(root, 70)
root = insert(root, 40)
root = insert(root, 10)
root = insert(root, 1)
root = insert(root, 50)
root = insert(root, 90)
inOrder(root)
search(root , 40)
search(root , 4)
 ## root hamesha 20 hi rahega chahe kuch bhi ho jaye   