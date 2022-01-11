Description
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Sample I/O
Example 1
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
  
  
This question is similart with question 323. Number of Connected Components in an Undirected Graph For this question,

As a tree, the the number of edges must equal to the number of nodes - 1.
If the given input can build up one valid tree, then there should be only one 
complete graph which include all nodes.
If the number of edges is the number of nodes - 1, we use BFS start from a certain 
node and find all related to this node and append them to the visited set. If the final 
size of the visited set is not equal to the number of nodes. That means there are more 
than 1 graph can be built by given input. Which is False

Code (BFS)
def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:return False
        dist = collections.defaultdict(list)
        for n1,n2 in edges:
            dist[n1].append(n2)
            dist[n2].append(n1)
        visited=set()
        queue=collections.deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for related in dist[node]:
                if related not in visited:
                    visited.add(related)
                    queue.append(related)
        return len(visited)==n
BigO
Build graph will take O(n) and traversal all number will take O(n). In total is O(2n) 
where n is the given as the size of the index.  
