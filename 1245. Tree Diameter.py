Question:
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  
Each node has labels in the set {0, 1, ..., edges.length}.



Solution: DP

https://programmerall.com/article/64621125882/

Intuition
For all nodes in the diameter, only one node is allowed that both left edge 
and right edge are used. So we could use a DFS to get this diameter.

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        adj = defaultdict(list)
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)
        visited = set()
        root = edges[0][0]
        visited.add(root)
        return max(self._helper(root, adj, visited))

    def _helper(self, node, adj, visited):
        visited.add(node)
        m1, m2, closed = 0, 0, 0
        for child in adj[node]:
            if child in visited:
                continue
            m, m_closed = self._helper(child, adj, visited)
            m += 1
            _, m1, m2 = sorted([m1, m2, m])
            closed = max(closed, m_closed)
        closed = max(closed, m1 + m2)
        return max(m1, m2), closed
