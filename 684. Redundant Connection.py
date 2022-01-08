Approach #1: DFS [Accepted]
Intuition and Algorithm

For each edge (u, v), traverse the graph with a depth-first search to see if we can 
connect u to v. If we can, then it must be the duplicate edge.


class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
            
            

Complexity Analysis

Time Complexity: O(N^2) where N is the number of vertices (and also the number of edges) in the graph. 
In the worst case, for every edge we include, we have to search every previously-occurring edge of the graph.

Space Complexity: O(N). The current construction of the graph has at most N nodes.
