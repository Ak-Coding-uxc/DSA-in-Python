class Node:
    def __init__(self, value ):
        self.data = value
        self.left = None
        self.right = None

def insert(root,value):
        if(root == None):
            return Node(value)
        if(root.data == value):
            return root
        if(root.data > value):
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data , end = " ")
        inOrder(root.right)

def search(root,value):
        if(root == None):
            print("Element not found" , end = "\n")
            return
        if(root.data == value):
            print("Element Found" , end = "\n")
            return
        if(root.data > value):
            search(root.left, value)
        else:
            search(root.right, value)

root = insert(None,20)
root = insert(root, 15)
root = insert(root,30)
root = insert(root,40)
root = insert(root,12)
root = insert(root,18)
root = insert(root,25)
root = insert(root,50)

inOrder(root)

search(root,50)
search(root, 90)
# always update root


""" 
# Time Complexity
= seraching = O(logn)
= insertion(for 1 element) = O(log n)
= for full tree creation = O(n log n)

 """



