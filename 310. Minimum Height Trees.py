Question:
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges, you can choose any node of the tree as the root. 
When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height
are called minimum height trees (MHTs). Return a list of all MHTs' root labels. The height of a rooted tree is the number of 
edges on the longest downward path between the root and a leaf.
 
Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT. 
       0              1                2               3
       |           /  |  \             |               |
       1          0   2   3            1               1
     /   \                           /   \           /   \    
    2     3                        0       3        0     2
 
 
 
Solution: Topological Sorting + BFS
Related to Course Schedule and Course Schedule II

we can rephrase the problem as finding out the nodes that are overall close to all other nodes, especially the leaf nodes.
If we view the graph as an area of circle, and the leaf nodes as the peripheral of the circle, then what we are looking for are
actually the centroids of the circle, i.e. nodes that is close to all the peripheral nodes (leaf nodes).
-If the number of nodes is even, then there would be two centroids.
-If the number of nodes is odd, then there would be only one centroid.
The problem is now reduced down to looking for all the centroid nodes in a tree-alike graph, which in addition are no more than two.
The idea is that we trim out the leaf nodes layer by layer, until we reach the core of the graph, which are the centroids nodes.

trim

Once we trim out the first layer of the leaf nodes (nodes that have only one connection), some of the non-leaf nodes would become leaf nodes.
The trimming process continues until there are only two nodes left in the graph, which are the centroids that we are looking for.
The above algorithm resembles the topological sorting algorithm which generates the order of objects based on their dependencies. 
For instance, in the scenario of course scheduling, the courses that have the least dependency would appear first in the order.
In our case, we trim out the leaf nodes first, which are the farther away from the centroids. At each step, the nodes we trim out 
are closer to the centroids than the nodes in the previous step. At the end, the trimming process terminates at the centroids nodes.

Implementation

Given the above algorithm, we could implement it via the Breadth First Search (BFS) strategy, to trim the leaf nodes layer by layer (i.e. level by level).
Initially, we would build a graph with the adjacency list from the input. We then create a queue which would be used to hold the leaf nodes.
At the beginning, we put all the current leaf nodes into the queue. We then run a loop until there is only two nodes left in the graph.
At each iteration, we remove the current leaf nodes from the queue. While removing the nodes, we also remove the edges that are 
linked to the nodes. As a consequence, some of the non-leaf nodes would become leaf nodes. And these are the nodes that would be
trimmed out in the next iteration.
The iteration terminates when there are no more than two nodes left in the graph, which are the desired centroids nodes.


    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
                      remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves
            
        # The remaining nodes are the centroids of the graph
        return leaves
