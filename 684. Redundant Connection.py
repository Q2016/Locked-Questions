Question:
In this problem, a tree is an undirected graph that is connected and has no cycles. You are given a graph that started as a tree with n 
nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an 
edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an 
edge between nodes ai and bi in the graph. Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there 
are multiple answers, return the answer that occurs last in the input.
1----2
|  /
3
Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]    


Solution: DFS
For each edge (u, v), traverse the graph with a depth-first search to see if we can connect u to v. If we can, then it must be the duplicate edge.

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
