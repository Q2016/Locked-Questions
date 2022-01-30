Question:
Given a binary search tree and a node in it, find the in-order successor of that node in the BST. The successor of a node p 
is the node with the smallest key greater than p.val. You will have direct access to the node but not to the root of the tree. 
Each node will have a reference to its parent node. Follow up: Could you solve it without looking up any of the node's values?

Example 1:
Input: tree = [2,1,3], node = 1, Output: 2, Explanation: 1's in-order successor node is 2. Note that both the node and the 
return value is of Node type.


Solution: Similar to 285. Inorder Successor in BST, I dont like it.

    def inorderSuccessor(self, node: "Node") -> "Node":
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
