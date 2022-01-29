Question:
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.
Note: A subtree must include all of its descendants. Follow up: Can you figure out ways to solve it with O(n) time complexity?

Example:
     10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is 5. The return value is the subtree's size, which is 3.


Solution: 

Similar to 98. Validate Binary Search Tree at each 

class Solution :
     def largestBSTSubtree(root):
        res = 0 ;
        dfs(root, res);
        return res;
    
     def dfs(root, res) :
         if (!root) :
               return 
         d = count(root, INT_MIN, INT_MAX);
         if (d != - 1 ) :
               res = max(res, d);
             return 
         dfs(root -> left, res);
         dfs(root -> right, res);
     
     # checks if BST, then counts number of left and right
     def count(root, mn, mx) :
         if (!root) :
               return  0 ;
         if (root.val <= mn or root.val >= mx) 
               return - 1 ;
         left = count( root.left, mn, root.val);
         if (left == - 1 ) :
               return - 1 ;
         right = count(root.right, root.val, mx);
         if (right == - 1 ) :
               return - 1 ;
         return left + right + 1 ;



Rewriting above, Solution two:

class Solution :
     def largestBSTSubtree(root) :
         if (!root) :
               return  0 
         if (isValid(root, INT_MIN, INT_MAX)) : 
               return count(root)
         return max(largestBSTSubtree(root.left), largestBSTSubtree (root.right))
    
     def isValid(root, mn, mx) :
         if (!root) 
               return  True 
         if (root.val <= mn or root.val >= mx) 
               return  False
         return isValid(root.left, mn, root.val) and isValid(root.right, root.val, mx)
    
     def count(root) :
         if (!root) 
               return  0 
         return count(root.left) + count(root.right) + 1 
    
 

Now if we want to solve the problem with the time complexity of O(n): The idea is to first 
recurse to the leftmost child node, and then recurse layer by layer. 
 

Solution three:

class Solution :

     def largestBSTSubtree(root) :
          res = 0  
          mn = INT_MIN 
          mx = INT_MAX
          isValidBST(root, mn, mx, res)
          return res;
    
     def isValidBST(root, mn, mx, res) :
          if (!root): 
               return 
          
          left_cnt = 0  
          right_cnt = 0
          left_mn = INT_MIN
          right_mn = INT_MIN 
          left_mx = INT_MAX 
          right_mx = INT_MAX
          
          isValidBST(root.left, left_mn, left_mx, left_cnt)
          isValidBST(root.right, right_mn, right_mx, right_cnt)
         
          if ((!root.left or root.val > left_mx) and (!root.right or root.val < right_mn)) :
               res = left_cnt + right_cnt + 1 
               mn = left_mn if (root.left) else root.val
               mx = right_mx if (root.right) else root.val
          else :
               res = max(left_cnt, right_cnt) 
        
 




