Question:
Given a binary tree where all the right nodes are either leaf nodes with a sibling 
(a left node that shares the same parent node) or empty, flip it upside down and turn 
it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  

                                    
                                    
Solution:
                                    
Process level by level.

    def upsideDownBinaryTree(self, root):

        if root is None:
            return None
        if root.left is None:
            return root

        new_root, prev_root = None, None
        while root.left is not None:
            if prev_root is None:
                new_root = TreeNode(root.left.val)
                new_root.left = root.right
                new_root.right = TreeNode(root.val)
            else:
                new_root = TreeNode(root.left.val)
                new_root.left = root.right
                new_root.right = prev_root
            prev_root = new_root
            root = root.left

        return new_root                                  
