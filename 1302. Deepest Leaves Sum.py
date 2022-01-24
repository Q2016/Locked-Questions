Question:
Given the root of a binary tree, return the sum of values of its deepest leaves.
 
Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15    

                    1
                 /     \
               2         3  
            /    \         \   
          4       5          6
         /                     \ 
        7                       8
    
    
Solution: BFS    

    def deepestLeavesSum(self, root):
        q = [] 
        res =  []
        t = []
        if root is None:
            return res
        q.append(root)
        while q:
            t=[]  #empty list for each level
            level = len(q)
            while level != 0:
                temp = q.pop(0)
                level -= 1 
                t.append(temp.val)
                if temp.left:
                    q.append(temp.left) ###storing elemets of the tree level wise
                if temp.right:    
                    q.append(temp.right) ###storing elemets of the tree level wise
            res.append(t) ###final level stored in t
        return sum(t)
