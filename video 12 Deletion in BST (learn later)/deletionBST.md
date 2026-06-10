# Learn some terminalogy before learning deletion in BST.
inorder =>
- used to find bst is correct or not
- print values in increasing order.

successor  = next element
predessor = previous elemtn

# for ex:- 
values = 10 , 8 , 30 , 6 , 9 , 25 , 40 , 20, 50
                               10
              8                               30 
                                    25                     40
       6            9        20                                    50

inorder traversal of tree = 6, 8, 9, 10, 20, 25, 30, 40, 50
* inorder successor of 25 = 30
* inorder predessor of 25 = 20

steps to find inorder successor of 10
- one step towards right 
and then left most element.

steps of find inorder predessor
- one step towards left
and then right most element.

# cases of deletion

case 1:- Deleion of leaf(0 child)

case 2:- Deletion of node having one child.

case 3:- deltion of node having two childs.

need parent node address to delete child.


### It is very hard to learn tree. What to do now ?