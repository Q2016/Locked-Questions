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


from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
            
        visited = {0}
        res = [0]
        self.dfs(0, graph, visited, res)
        
        return res[0]
    
    def dfs(self, city: int, graph: dict, visited: set, res: List[int]) -> None:
        
	visited.add(city)
        
        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                res[0] += cost
                self.dfs(neighbor, graph, visited, res)
