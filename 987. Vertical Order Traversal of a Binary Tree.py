Question:
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. 
The root of the tree is at (0, 0). The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting 
from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort 
these nodes by their values. Return the vertical order traversal of the binary tree.


Solution:
Approach 1: queue + hash map
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231256/python-queue-%2B-hash-map  

class Solution(object):
    def verticalTraversal(self, root):
        g = collections.defaultdict(list) 
        queue = [(root,0)]
        while queue:
            new = []
            d = collections.defaultdict(list)
            for node, s in queue:
                d[s].append(node.val) 
                if node.left:  new += (node.left, s-1), 
                if node.right: new += (node.right,s+1),  
            for i in d: g[i].extend(sorted(d[i]))
            queue = new
        return [g[i] for i in sorted(g)]
      
      
Approach 2: Simple dfs
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/777584/Python-Simple-dfs-explained  
  
First of all, I want to mention, that problem statement is not clear at all, I need to go to comments to understand, what order they expect us to return nodes in levels. So, we have X coordinate and Y coordinate, we need to group them by X coordinate. If we have the same X coordinate, we need to check:

First put nodes with higher Y coordinates, that ones, which are close to root
If two nodes have the same Y coordinate also, we need to put small values before big values.
Let us define dic, where we create our vertical layers, and self.min_l and self.max_l be minimal and maximal numbers of vertical layers. Let us start to traverse our graph, using dfs, with parameters:

root is current node we are in now
lvl_h is horizontal coordinate, that is X
lvl_v is vertical coordinate, that is -Y: note, that I increase my Y coordinate as I go down, it is simpler to deal in this way.
Inside dfs we do the following steps:

Update self.min_l and self.max_l.
Add lvl_v and root.val pair to our dictionary. We need to add pair to sort it after.
Finally, visit left and right children if it is possible.
In the end, we need to sort each level, and add it to final list of lists.

Complexity: Usual dfs traversal will take O(n) time. However we need to sort each level, before we give final result. Let us have w_1, ..., w_h nodes on each layer. then we need to do w_1 log w_1 + ... + w_h log w_h < n * log W operations, where W is width of the biggest layer. So, complexity is O(n log W), which potentially can be O(n log n), because the widest level can have upto n/2 nodes. Space complexity is O(n).

class Solution:
    def verticalTraversal(self, root):
        dic = defaultdict(list)
        self.min_l, self.max_l = float("inf"), -float("inf")
        def dfs(root, lvl_h, lvl_v):
            self.min_l = min(lvl_h, self.min_l)
            self.max_l = max(lvl_h, self.max_l)
            dic[lvl_h].append((lvl_v, root.val))
            if root.left:  dfs(root.left,  lvl_h-1, lvl_v+1)
            if root.right: dfs(root.right, lvl_h+1, lvl_v+1)
        
        dfs(root, 0, 0)
        out = []
        for i in range(self.min_l, self.max_l + 1):
            out += [[j for i,j in sorted(dic[i])]]
        return out  
