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



    
    
    
    
    
    
    
    
    
    
    
Solution:
From this link:  https://www.youtube.com/watch?v=l1hSUOaXLxc 
  
In-order gives the list in sorted order
Save the first and the last element since we need to link them
traverse to the last left node that exists and then start to bounce back



    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        self.first=None
        self.last=None
        
        self.inorder_link(root)
        
        
   def inorder_link(self, node):
        if node:
            self.inorder_link(node.left)

            if not self.last:
                self.first=node
            else:
                node.left=self.last
                self.last.right=node

            self.last=node

            self.inorder_link(node.right)
          
          
          
        
        
      
      
               
          
          
Time Complexity: O(N).
Space Complexity: O(N).
