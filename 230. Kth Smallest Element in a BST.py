Question:
Given the root of a binary search tree, and an integer k, return the kth smallest value of all the values of the nodes in the tree.    


Solution: Inorder
    
To solve the problem, one could use the property of BST : inorder traversal of BST is an array sorted in the ascending order.    
    
    
def kthSmallest_dfs_early_stopping(self, root, k):
	res = []
	
    def inorder(node):
		if not node: return
		inorder(node.left)
		if len(res) == k:
			return
		res.append(node.val)
		inorder(node.right)
        
	inorder(root)
	return res[-1] 

    
    
Complexity Analysis
Time complexity : O(N) to build a traversal.
Space complexity : O(N) to keep an inorder traversal.    
