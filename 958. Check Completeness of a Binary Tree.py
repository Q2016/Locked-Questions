Question:
Given the root of a binary tree, determine if it is a complete binary tree. In a complete binary tree, every level, except possibly the last, 
is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.    












Solution:level-order traversal
    
The level-order traversal array of a complete binary tree will never have a null node in between non-null nodes. If we encounter a null node, 
all the following nodes should also be null, otherwise it's not complete.


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        have_null = False
        Q = [root]
        
        while Q:
            cur_node = Q.pop(0)
            if not cur_node: 
                have_null = True
                continue
            if have_null: return False
            Q.append(cur_node.left)
            Q.append(cur_node.right)
            
        return True    

    
Time O(N) 
Space O(N)    
