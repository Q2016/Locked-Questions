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
 
 
 
 
 
 
 
 
The idea is that first connect the graph, then start removing leaves from outside toward inward, when
the number of node is less than 2, we have the center.
 
Solution: Topological Sorting + BFS
Related to Course Schedule and Course Schedule II

https://www.youtube.com/watch?v=OsvbLAaRmu8

  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
     if n==1:
       return [0]
     
     graph=defaultdict(list)
     
     for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
     
     leaves = [node for node in graph.keys() if len(graph[node])==1]
     
     while n>2:
        n-=len(leaves)
        new_leaves=set()
        for leave in leaves:
           neighbor=graph[leave].pop()
           graph[neighbor].remove(leave)

           if len(graph[neighbor])==1:
              new_leaves.add(neighbor)

        leaves=new_leaves
      
     return leaves
       
      
     

     
        
