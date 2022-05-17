Question:
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array 
graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads 
to a terminal node.
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:
Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.











Solution: Depth-First Search [Accepted]

As in Approach #1, the crux of the problem is whether you reach a cycle or not.

Let us perform a "brute force": a cycle-finding DFS algorithm on each node individually. 
This is a classic "white-gray-black" DFS algorithm that would be part of any textbook on DFS. 
We mark a node gray on entry, and black on exit. If we see a gray node during our DFS, it must 
be part of a cycle. In a naive view, we'll clear the colors between each search.

We can improve this approach, by noticing that we don't need to clear the colors between each search.

When we visit a node, the only possibilities are that we've marked the entire subtree black 
(which must be eventually safe), or it has a cycle and we have only marked the members of that 
cycle gray. So indeed, the invariant that gray nodes are always part of a cycle, and black nodes 
are always eventually safe is maintained.

In order to exit our search quickly when we find a cycle (and not paint other nodes erroneously), 
we'll say the result of visiting a node is true if it is eventually safe, otherwise false. This allows 
information that we've reached a cycle to propagate up the call stack so that we can terminate our search early.


class Solution(object):
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != white:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True
        
        #The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.
        return filter(dfs, range(len(graph))) 
    
    
Complexity Analysis
Time Complexity: O(N + E), where N is the number of nodes in the given graph, and E is the total number of edges.
Space Complexity: O(N) in additional space complexity.    
