Question:
Given the root of a complete binary tree, return the number of the nodes in the tree.
Design an algorithm that runs in less than O(n) time complexity. 

The O(n) solution is:
  
    def countNodes(self, root: Optional[TreeNode]) -> int:      
        if root==None:
            return 0  
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
      
But the problem is asking for less than O(n) so:

  
  
  
  
  
  
  
  
  
  
  
Solution: 

  
In a complete tree at level l we have 2^l leefs
Number of total nodes will follow this patern: 
level   # of nodes 
    1->1
    2->3
    3->7
    
then we check the left and right depth, if they are equal the tree is full if not we break it to
left tree and right tree and recursivly continue

https://www.youtube.com/watch?v=i_r2uKbwHCU

compare the depth between left sub tree and right sub tree.
A, If it is equal, it means the left sub tree is a full binary tree
B, It it is not , it means the right sub tree is a full binary tree

 class Solution:
      def countNodes(self, root):
          if root==None: return 0
          left, right=root, root
          h_l, h_r=0, 0

          while left !=None:
              h_l +=1
              left=left.left

          while right !=None:
              h_r +=1
              right=right.right

          if h_l==h_r: return (1<<h_l)-1

          return 1+ self.countNodes(root.left)+self.countNodes(root.right)

        
time complexity:
  https://www.youtube.com/watch?v=CvrPf1-flAA
    
O(log N *log N)    
