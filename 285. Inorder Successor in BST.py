Question:
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Example 1:
Input: root = [2,1,3], p = 1, Output: 2

  2
 / \
1   3

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6, Output: null
      5
     / \
    3   6
   / \
  2   4
 /   
1









Solution: Inorder  (Left, Root, Right)

read: Binary Search Trees_ BST Explained with Examples.pdf  
  
The in-order successor of a node is the left-most node in its right sub-tree, if exists. If not, then it is the root of the 
smallest left sub-tree this node is in.


    def inorderSuccessor(self, root, p):

        if root=None: 
            return None
        
        cur=root
        pre=None
        
        while cur !=None :
            if cur.val > p.val:
                pre=cur
                cur=cur.left
            else:
                cur=cur.right
            
        return pre
