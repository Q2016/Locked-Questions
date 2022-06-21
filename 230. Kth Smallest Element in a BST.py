Question:
Given the root of a binary search tree, and an integer k, return the kth smallest value of all the values of the nodes in the tree.    
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, 
how would you optimize?

	
	
	
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


	
Approach 2: Iterative Inorder Traversal
The above recursion could be converted into iteration, with the help of stack. This way one could speed up the solution because 
there is no need to build the entire inorder traversal, and one could stop after the kth element.	
	
	
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right	
		
		
Complexity Analysis

Time complexity: O(H+k), where H is a tree height. This complexity is defined by the stack, which contains at least H+k elements, 
since before starting to pop out one has to go down to a leaf. This results in O(logN+k) for the balanced tree and O(N+k) for completely 
unbalanced tree with all the nodes in the left subtree.

Space complexity: O(H) to keep the stack, where H is a tree height. That makes O(N) in the worst case of the skewed tree, O(logN) in 
the average case of the balanced tree.		


Follow up

https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/

What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Click here to learn how to insert a node into a BST and delete a node from a BST, the time complexity of these operations is O(H)O(H), where HH is a height of the binary tree. H = \log NH=logN for the balanced tree and H = NH=N for a skewed tree.

Hence without any optimisation insert/delete + search of kth element has O(2H + k)O(2H+k) complexity. How to optimise that?

That's a design question, basically we're asked to implement a structure which contains a BST inside and optimises the following operations :

Insert

Delete

Find kth smallest

Seems like a database description, isn't it? Let's use here the same logic as for LRU cache design, and combine an indexing structure (we could keep BST here) with a double linked list.

Such a structure would provide:

O(H)O(H) time for the insert and delete.

O(k)O(k) for the search of kth smallest.

bla

The overall time complexity for insert/delete + search of kth smallest is O(H + k)O(H+k) instead of O(2H + k)O(2H+k).

Complexity Analysis

Time complexity for insert/delete + search of kth smallest: O(H + k)O(H+k), where HH is a tree height. O(\log N + k)O(logN+k) in the average case, O(N + k)O(N+k) in the worst case.

Space complexity : O(N)O(N) to keep the linked list.
