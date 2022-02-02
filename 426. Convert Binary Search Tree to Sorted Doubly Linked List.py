Question:  
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous 
and next pointers in a doubly-linked list.        4
                                                /   \
                                              2       5
                                            /   \
                                          1       3
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. 
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is 
the first element. The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points 
to is the smallest element of the linked list. Specifically, we want to do the transformation in place. After the transformation, the 
left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the 
pointer to the first element of the linked list.

              ------>  ------>  ------>  ------>
head -----> 1 <------2 <------3 <------4 <------5 --
            |                                      |
            <---------------------------------------

Solution:
Find the BST tree values in ascending order. Then use the BST tree values to build a Circular Doubly-Linked List.

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
