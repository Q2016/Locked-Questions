Question:
Given a graph, return true if and only if it is bipartite.
Recall that a graph is bipartite if we can split it's set of nodes into
two independent subsets A and B such that every edge in the graph has
one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j
for which the edge between nodes i and j exists. 
Each node is an integer between 0 and graph.length - 1.
There are no self edges or parallel edges: graph[i] does not contain i,
and it doesn't contain any element twice.

 Example 1:
 Input: [[1,3], [0,2], [1,3], [0,2]]
 Output: true
 Explanation: 
 The graph looks like this:
 0----1
 |    |
 |    |
 3----2
 We can divide the vertices into two groups: {0, 2} and {1, 3}.
  
 Example 2:
 Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
 Output: false
 Explanation: 
 The graph looks like this:
 0----1
 | \  |
 |  \ |
 3----2
We cannot find a way to divide the set of nodes into two independent ubsets.










Solution: Graph coloring
    
  
  Link from: https://www.youtube.com/watch?v=YNNLcENsB_4
  
  
class Solution(object):
    def isBipartite(self, graph):

        seen = {} # A or B, 0 or 1
        for node in xrange(len(graph)):
            if node not in seen:
                seen[node]=0
                stack = [node]
    
                while stack:
                    cur = stack.pop()
                    for neighbor in graph[cur]:
                        if neighbor not in seen:
                            stack.append(neighbor)
                            seen[neighbor]=seen[cur]^1 # flip
                        elif seen[neighbor]==seen[cur]:
                            return False

        return True

    
Time:  O(|V| + |E|)
Space: O(|V|)    
