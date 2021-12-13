The O(n) solution is:
  
  class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root==None:
            return 0
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
      
      
But the problem is asking for less than O(n) so:

My solution:
  
  
  
  
  
  
  
  
 https://leetcode.com/problems/count-complete-tree-nodes/discuss/533887/Python-sol-by-binary-search.-90%2B-w-Visualization 
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        
        def helper( node: TreeNode):
            
            root = node
            
            if not node:
                
                # Quick response for empty tree
                return 0
            
            
            height = 0
            while node:
                node = node.left
                height += 1
            
            
            if height == 1:
                
                # Quick response for tree with one level only
                return 1
            
            
            # boundary of node numbering on last level
            
            left, right = 2 ** (height - 1), (2 ** height - 1)
            
            # For complete binary tree, the leftmost node on last level must exist
            
            last_exist = left
            
            
            # Launch binary search to find the numbering of last non-empty node on last level
            
            while left <= right:
                cur = root
                mid = left + (right-left) // 2
                
                # path finding for node with numbering with mid
                for h in range(height-2, -1, -1):
                    
                    mask =  1 << h
                    
                    if mid & mask :
                        cur = cur.right
                        
                    else:
                        cur = cur.left
                    
                    mask >>= 1
                    
                if cur is not None:
                    # update latest finding on last level
                    last_exist = mid
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return last_exist
        
        # -------------------------------
        
        return helper( root )
  
