Question:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants”
                     3
                   /   \
                 5        1
               /   \     /  \
              6     2   0    8
                   / \
                  7   4
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.    

    
  
  
  
  
  
  
Solution:   (refer to 235. not identical)
https://www.youtube.com/watch?v=VG5w_VVAgH4

we return whenever, we find p or q i.e we find our left and right
  
    def lowestCommonAncestor(self, root, p, q):

        def dfs(cur):
            if not cur:
              return None
            
            if cur==p or cur ==q:
              return cur
            
            left=dfs(cur.left)
            right=dfs(cur.right)
            
            # first case
            if left and right:
              return cur
            
            # second case
            return left if left else right
          


