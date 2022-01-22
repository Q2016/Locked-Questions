Question:

Given the edges of a directed graph, and two nodes source and destination of this graph, determine whether 
or not all paths starting from source eventually end at destination, that is:

At least one path exists from the source node to the destination node
If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
The number of possible paths from source to destination is a finite number.
Return true if and only if all roads from source lead to destination.

Example 1:
Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
Output: false
Explanation: It is possible to reach and get stuck on both node 1 and node 2.

Example 2:
Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
Output: false
Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.

Example 3:
Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
Output: true

  
  
Solution: DFS
Use depth-first search to see if all paths end with the destination node.
Time Complexity: O(N).
Space Complexity: O(N).
  
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
   
        adjacency_list = [set() for i in range(n)]
        
        for edge in edges:            
            adjacency_list[edge[0]].add(edge[1])
            
        return self.helper(source, destination, adjacency_list, set())
        
                
        
    def helper(self, node, destination, adjacency_list, visited):
        if node in visited:
            return False

        if node != destination and not adjacency_list[node]:
            return False
        
        if node == destination and len(adjacency_list[node]) > 0:
            return False
        
        if node == destination:
            return True
        
        visited.add(node)
        
        
        for neighbor in adjacency_list[node]:   
            if not self.helper(neighbor, destination, adjacency_list, visited):
                return False
            
        visited.remove(node)
        
        
        return True

