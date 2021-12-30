Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example 1:

Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

Output: null



Solution
The in-order successor of a node is the left-most node in its right sub-tree, 
if exists. If not, then it is the root of the smallest left sub-tree this node is in.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None
        if p.right is not None:
            node = p.right
            successor = node
            while node.left is not None:
                node = node.left
                successor = node
            return successor
        else:
            node = root
            successor = None
            while True:
                if node is None:
                    return None
                if node == p:
                    break
                elif p.val < node.val:
                    successor = node
                    node = node.left
                else:
                    node = node.right

        return successor
