Solution image:
https://ttzztt.gitbooks.io/lc/content/string/convert-binary-search-tree-to-sorted-doubly-linked-list.html
  


Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:



We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.



Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.



Thoughts:

Find the BST tree values in ascending order. Then use the BST tree values to build a Circular Doubly-Linked List.


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        node_values = []
        
        self.get_node_values(root, node_values)
        
        
        first_node = Node(node_values[0])
        prev = first_node
        
        
        for value in node_values[1:]:
            new_node = Node(value)
            new_node.left = prev
            prev.right = new_node
            prev = new_node
            
        prev.right = first_node
        first_node.left = prev
        
        return first_node
        
            
    def get_node_values(self, root, results):
        if not root:
            return
                
        self.get_node_values(root.left, results)        
        results.append(root.val)
        self.get_node_values(root.right, results)
                
Time Complexity: O(N).
Space Complexity: O(N).
