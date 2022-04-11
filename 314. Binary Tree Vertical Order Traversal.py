Question:
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Examples 1:
Input: [3,9,20,null,null,15,7], Output: [[9],[3,15],[20],[7]]
   3
  / \
 /   \
9     20
     / \
    /   \
  15     7 


   
   
   
   
Solution: 
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231318/How-is-this-different-from-%22314.-Binary-Tree-Vertical-Order-Traversal%22/258772/

The difference is the way of handling nodes that have same x and y coordinates (for picture above link):

-LC 314 If two nodes are in the same row and column, the order should be from left to right.
When two nodes are in the same position, the order is decided by their x coordinates (node from the left subtree comes first). node6 -> node3
-LC 987 If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
When two nodes are in the same position, the order is decided by their values (node with smaller value comes first). node3 -> node6    



   
      
      
      
