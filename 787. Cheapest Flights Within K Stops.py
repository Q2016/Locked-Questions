Question:
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates 
that there is a flight from city fromi to city toi with cost pricei. You are also given three integers src, dst, and k, return the cheapest price 
from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.    








Solution: Dijkstra
	
A good case to practice Dijkstra.
To implement Dijkstra, we need a priority queue to pop out the lowest weight node for next search. In this case, the weight would be the 
accumulated flight cost. So my node takes a form of (cost, src, k). cost is the accumulated cost, src is the current node's location, k is 
stop times we left as we only have at most K stops. I also convert edges to an adjacent list based graph g.
Use a vis array to maintain visited nodes to avoid loop. vis[x] record the remaining steps to reach x with the lowest cost. If vis[x] >= k, 
then no need to visit that case (start from x with k steps left) as a better solution has been visited before (more remaining step and lower 
cost as heappopped beforehand). And we should initialize vis[x] to 0 to ensure visit always stop at a negative k.
Once k is used up (k == 0) or vis[x] >= k, we no longer push that node x to our queue. Once a popped cost is our destination, we get our 
lowest valid cost. For Dijkstra, there is not need to maintain a best cost for each node since it's kind of greedy search. It always chooses 
the lowest cost node for next search. So the previous searched node always has a lower cost and has no chance to be updated. The first time we 
pop our destination from our queue, we have found the lowest cost to our destination.

def findCheapestPrice(n, flights, src, dst, K):
	graph = collections.defaultdict(dict)
	for s, d, w in flights:
		graph[s][d] = w
	pq = [(0, src, K+1)]
	vis = [0] * n
	while pq:
	   w, x, k = heapq.heappop(pq)
	   if x == dst:
		return w
	   if vis[x] >= k:
		continue
	   vis[x] = k
	   for y, dw in graph[x].items():
		heapq.heappush(pq, (w+dw, y, k-1))
	return -1


Python heapq doesn't support update heap node's weight. But if you implement your own heap structure and support that function, 
you can maintain a n-size heap and time complexity is O((m + n)logn). m is number of edges and n is number of nodes. And it can be 
improved to O(m + nlogn) with a Fibonacci heap where a delete min costs logn but an update cost costs constant time.    
