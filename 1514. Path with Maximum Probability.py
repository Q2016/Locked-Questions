Question:
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] 
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return
its success probability.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.	
 		0
	0.5   /   \  0.2
	     /     \
            1 ----- 2       	
	       0.5
	
Solutioin: Bellman Ford (first) or Dijkstra (second):

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g, dq = defaultdict(list), deque([start])
        for i, (a, b) in enumerate(edges):
            g[a].append([b, i])
            g[b].append([a, i])
        p = [0.0] * n    
        p[start] = 1.0
        while dq:
            cur = dq.popleft()
            for neighbor, i in g.get(cur,[]):
                if p[cur] * succProb[i] > p[neighbor]:
                    p[neighbor] = p[cur] * succProb[i]
                    dq.append(neighbor)
        return p[end]
Analysis:
Time: O(n * E), space: O(n + E), where E = edges.length.
		
		
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        p, g = [0.0] * n, defaultdict(list)
        for index, (a, b) in enumerate(edges):
            g[a].append((b, index))
            g[b].append((a, index))
        p[start] = 1.0
        heap = [(-p[start], start)]    
        while heap:
            prob, cur = heapq.heappop(heap)
            if cur == end:
                return -prob
            for neighbor, index in g.get(cur, []):
                if -prob * succProb[index] > p[neighbor]:
                    p[neighbor] = -prob * succProb[index]
                    heapq.heappush(heap, (-p[neighbor], neighbor))
        return 0.0
Analysis:
Time: O((n + E) * logE), space: O(n + E), where E = edges.length.
		


Bellman Ford algorithm:
https://algs4.cs.princeton.edu/44sp/
https://algs4.cs.princeton.edu/44sp/BellmanFordSP.java.html
https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture14.pdf
https://en.wikipedia.org/wiki/Bellman–Ford_algorithm
https://www.geeks for geeks.org/bellman-ford-algorithm-dp-23/(remove the 2 spaces among the links to make it valid)

Dijkstra's algorithm:
https://algs4.cs.princeton.edu/44sp/
https://algs4.cs.princeton.edu/44sp/DijkstraSP.java.html
https://en.wikipedia.org/wiki/Dijkstra's_algorithm
https://www.geeks for geeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ (remove the 2 spaces among the links to make it valid)

Similar problems:
407. Trapping Rain Water II
499. The Maze III
505. The Maze II
743. Network Delay Time
787. Cheapest Flights Within K Stops
1631. Path With Minimum Effort
