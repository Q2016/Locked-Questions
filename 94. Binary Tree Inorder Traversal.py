Question:
Given the root of a binary tree, return the inorder traversal of its nodes' values.    


https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/All-DFS-traversals-(preorder-inorder-postorder)-in-Python-in-1-line    
    
def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []
def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []




Complexity Analysis
Time complexity : O(n). The time complexity is O(n) because the recursive function is T(n) = 2 T(n/2)+1.
Space complexity : The worst case space required is O(n), and in the average case it's O(logn) where nn is number of nodes.
    
