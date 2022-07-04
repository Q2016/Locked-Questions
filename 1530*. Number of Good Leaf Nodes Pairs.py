Question:
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary
tree is said to be good if the length of the shortest path between them is less than or equal to 'distance'.
Return the number of good leaf node pairs in the tree.

Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. 
This is the only good pair.    
                    1
                 /    \
                2      3
                 \
                   4
    
    

    
    
    
    
    
 I dont understand this   
    
Solution: Postorder
    
My idea was to traverse from bottom to top (postorder) and keep track of the distance of the leaf 
nodes to each node. Once those leaf nodes meet a Lowest Common Ancestor, we can immediately check 
whether they are good pairs by checking if dist_from_leaf1_to_LCA + dist_from_leaf2_to_LCA <= distance. 
If so, we can increment the count by 1.
This works because for any leaf node pair, the shortest distance between those two nodes is 
always dist_from_leaf1_to_LCA + dist_from_leaf2_to_LCA. Each node will "pass up" the information of 
distances from all leaf nodes from the left to the current node and distances from all leaf nodes 
from the right to the current node in a list.
We can ensure that each node has leaf nodes on both sides by checking if the list returned from both 
sides are non-empty. Once a node has the distance information from both sides, we can check how many 
pairs are good pairs by calculating the distance between every pair of nodes. 
count += sum(l + r <= distance for l in left for r in right)


    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            count += sum(l + r <= distance for l in left for r in right)
            return [n + 1 for n in left + right if n + 1 < distance]
        
        dfs(root)
        return count

