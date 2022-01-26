Question:
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between 
two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads 
in one direction because they are too narrow. Roads are represented by connections where connections[i] = [ai, bi] 
represents a road from city ai to city bi. This year, there will be a big event in the capital (city 0), and many 
people want to travel to this city. Your task consists of reorienting some roads such that each city can visit the 
city 0. Return the minimum number of edges changed.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

	3 - 2
      /
    1	
  /	
0  - 4 - 5	


Solution: DFS
	
Start from node 0 (the capital) and dfs on the path and see if the path is
in the same direction as the traversal. If it is on the same direction that
means we need to reverse it because it can never get to the capital.


    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0    
        roads = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)
        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)    
        dfs(0, -1)
        return self.res
