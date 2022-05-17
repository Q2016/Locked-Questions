Question:
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.

Example 1:
Input: root = [1,null,0,0,1]   Output: [1,null,0,null,1]
  1                 1
    \                \  
     0      =>         0
    / \                 \
   0    1                 1
        
        
        
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.    
    
    
    
    
    
    
    
    
Solution: Recursion [Accepted]
    
Prune children of the tree recursively. The only decisions at each node are whether to prune the left child or the right child.
We'll use a function containsOne(node) that tells us whether the subtree at this node contains a 1, and prunes all subtrees that do not contain 1.
If for example, node.left subtree does not contain a one, then we should prune it via node.left = null.
Also, the parent needs to be checked. If for example the tree is a single node 0, the answer is an empty tree.    



class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def contains_one(node: TreeNode) -> bool:
            if not node: 
                return False
            # Check if any node in the left subtree contains a 1.
            left_contains_one = contains_one(node.left)
            # Check if any node in the right subtree contains a 1.
            right_contains_one = contains_one(node.right)
            # If the left subtree does not contain a 1, prune the subtree.
            if not left_contains_one: 
                node.left = None
            # If the right subtree does not contain a 1, prune the subtree.
            if not right_contains_one: 
                node.right = None
            # Return True if the current node or its left or right subtree contains a 1.
            return node.val or left_contains_one or right_contains_one

        # Return the pruned tree if the tree contains a 1, otherwise return None.
        return root if contains_one(root) else None
    
    
or

Use dfs(node) function which returns True only if all subtree has only zeroes. Evaluate it for left and right children: if for any of 
them answer is True, we cut this children. Also we return True if answer for both child is true and value of node is equal to zero. 
In the end, we check if answer is True and if it is, we return empty tree end if it is not, we return original root.

Complexity
Time complexity is O(n), space complexity is O(h).

Code
class Solution:
    def pruneTree(self, root):
        def dfs(node):
            if not node: return True
            left, right = dfs(node.left), dfs(node.right)
            if left: node.left = None
            if right: node.right = None
            return left and right and node.val == 0
        
        return root if not dfs(root) else None
    
    
Complexity Analysis

Time Complexity: O(N), where N is the number of nodes in the tree. We process each node once.
Space Complexity: O(N), the recursion call stack can be as large as the height H of the tree. In the worst case scenario, H=N, 
when the tree is skewed.    
