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

    
    
 Solution:   Recursive Approach

Traverse the tree in a DFS manner. The moment you encounter either of the nodes p or q, return some boolean flag. 
The flag helps to determine if we found the required nodes in any of the paths. The least common ancestor would then be 
the node for which both the subtree recursions return a True flag. It can also be the node 
which itself is one of p or q and for which one of the subtree recursions returns a True flag.

    def lowestCommonAncestor(self, root, p, q):

        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            # If the current node is one of p or q
            mid = current_node == p or current_node == q
            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node
            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
