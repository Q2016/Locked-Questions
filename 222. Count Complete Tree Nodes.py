The O(n) solution is:
  
  class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root==None:
            return 0
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
      
      
But the problem is asking for less than O(n) so:

My solution:
  
  
  
  
  
  
  
