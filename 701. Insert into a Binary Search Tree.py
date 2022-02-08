Question:
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST. Notice that there may exist multiple valid ways for the insertion, as long 
as the tree remains a BST after insertion. You can return any of them.
		 4                 4
	       /  \             /    \
	      2	   7          2       7
	    /  \	     / \     /
           1    3          1    3   5
Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]	

	
Solution: Recursive
	
If the root is empty, the new tree node can be returned as the root node. Otherwise compare root. val is related to the size of the target value:
If root.val is greater than the target value, indicating that the target value should be inserted into the left subtree of the root, and the 
problem becomes root. Insert the target value in the left and recursively call the current function;
If root.val is less than the target value, indicating that the target value should be inserted into the right subtree of the root, and the 
problem becomes root. Insert the target value in right and recursively call the current function.


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return TreeNode(val) 
        if root.val > val:  root.left = self.insertIntoBST(root.left, val)
        else: root.right = self.insertIntoBST(root.right, val)
        return root



Time Complexity: O(N)
Space Complexity: O(H) as considering recursion stack, takes place in internal memory, if not consider then O(1)
