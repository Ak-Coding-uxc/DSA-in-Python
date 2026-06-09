### Date => 9 June 2026.
Binary Tree != BST

## Binary Tree
binary tree is O(n)
- atmost 2 child.

## BST
- BST is O(log n)
- bst have 1 other condition.
=> left subtree is smaller than root and right subtree is larger than root value.

for ex:- 
                          50
            40                        100
    30               45         90                  100

total number of compression => height of tree = log n

what to learn 
1) insertion
2) search
insertion and search code is similar
3) Deletion => This is some tricky.

for ex of bst:-
20 , 30 , 15 , 25 , 40 , 50 , 23
20 is root node.
                             20
            15                                  30
                                      25                  40
                              23                              50

Interview questions of bst:
1) Print all elements of bst in increasing.
2) How check a valid BST.
3) Inorder Traversal of BST.
==> All 3 questions are same. 
beacause when printing in inorder traversal it print in increasing order.
inorder = 15 , 20 , 23 , 25 , 30 , 40 , 50.



