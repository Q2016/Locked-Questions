Question:
    
Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, if its parent node becomes a leaf node 
and has the value target, it should also be deleted (you need to continue doing that until you cannot).

Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed. 
After removing, new nodes become leaf nodes with value (target = 2) 







Solution: Recursive

    def removeLeafNodes(self, root, target):
        if root.left: root.left = self.removeLeafNodes(root.left, target)
        if root.right: root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root    

