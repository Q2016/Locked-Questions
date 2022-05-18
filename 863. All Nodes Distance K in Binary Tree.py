Question:
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all 
nodes that have a distance k from the target node. You can return the answer in any order.    















Solution:
If we know the parent of every node x, we know all nodes that are distance 1 from x. We can then perform a breadth first search 
from the target node to find the answer.
We first do a depth first search where we annotate every node with information about it's parent.
After, we do a breadth first search to find all nodes a distance K from the target    

class Solution(object):
    
    def distanceK(self, root, target, K):
        
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []
    
    
Complexity Analysis

Time Complexity: O(N), where N is the number of nodes in the given tree.
Space Complexity: O(N).    
