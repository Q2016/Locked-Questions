Question:
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. 
Each worker and bike is a 2D coordinate on this grid.
We assign one unique bike to each worker so that the sum of the Manhattan distances 
between each worker and their assigned bike is minimized.
The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.


Ex1:
  Input: 
workers = 
[[0,0],[2,1]]
, bikes = 
[[1,2],[3,3]]
Output: 
6
Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.

Ex2:
  Input: 
workers = 
[[0,0],[1,1],[2,0]]
, bikes = 
[[1,0],[2,2],[2,1]]
Output: 
4
Explanation: 
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. 
Both assignments lead to sum of the Manhattan distances as 4.



Solution: Dijkstra? --->heap



Code: Dijkstra on augmented path: 
def assignBikes(self, workers, bikes):
        distances = []     # distances[worker] is tuple of (distance, worker, bike) for each bike 
        for i, (x, y) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse = True)  # reverse so we can pop the smallest distance

        result = [None] * len(workers)
        used_bikes = set()
        queue = [distances[i].pop() for i in range(len(workers))]   # smallest distance for each worker
        heapq.heapify(queue)

        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(queue)
            if bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike
        return result
      
      
      
      
      O(n^2)
      
      class Solution:
    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> List[int]:
        ans, used = [-1] * len(W), set()
        for d, w, b in sorted([abs(W[i][0] - B[j][0]) + abs(W[i][1] - B[j][1]), i, j] for i in range(len(W)) for j in range(len(B))):
            if ans[w] == -1 and b not in used:
                ans[w] = b
                used.add(b)
        return ans
      
      
      


