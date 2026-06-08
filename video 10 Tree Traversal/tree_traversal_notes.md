focus on root value.
# first print left value then right value.

        1
    2       3

# root kabhi bhi print ho sakta ho h. 
ex:- 123 , 321(wrong r to l not alowed), 231 , 213 etc.
1 2 3 => root then l then r, its called Preorder traversal.
2 1 3 => L root R , its called Inorder Traversal.
2 3 1 => L R root , Postorder traversal.
# alwsays rule is left node print first.

ex:-
                          1
            3                        5
    2               4                           8

1) Preorder Traversal => Root -> Left subtree -> Right subtree
1  | left subtree 3  2  4 | right subtree  5  8
print root 
then go in root.left , then call recursion.

then again call recursion for right subtree
in root.right node.

2) Inorder :- 2 3 4 1 5 8

3) Postorder :- 2 4 3 8 5 1 
