Question:
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]    

                1
             /     \
           2         3
            \         \
             5         4

        
        
        
        
        
        
        
Do a level order and pop the left most node        
        
Solution: BFS
    
   def rightSideView(self, root):
      res=[]
      q=collections.deque([root])
      
      while q:
        rightSide=None
        qLen=len(q)
        
        for i in range(qLen):
          node=q.popleft()
          if node:
            rightSide=node
            q.append(node.left)
            q.append(node.right)
            
        if rightSide:
          res.append(rightSide)
          
      return res
 
    
            
