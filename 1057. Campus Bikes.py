On a campus represented as a 2D grid, there are Nworkers and Mbikes, with N <= M. 
Each worker and bike is a 2D coordinate on this grid.
Our goal is to assign a bike to each worker. Among the available bikes and workers, 
we choose the (worker, bike) pair with the shortest Manhattan distance between each other, 
and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the 
same shortest Manhattan distance, we choose the pair with the smallest worker index; if 
there are multiple ways to do that, we choose the pair with the smallest bike index). 
We repeat this process until there are no available workers.
The Manhattan distance between two points p1and p2is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|. 
Return a vector ansof length N, where ans[i]is the index (0-indexed) of the bike that the i-th worker is assigned to.

Example 1:
Input: 
workers = [[0,0],[2,1]], 
bikes = [[1,2],[3,3]]
Output: 
[1,0]
Explanation: 
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].

Example 2:
Input: 
workers = [[0,0],[1,1],[2,0]], 
bikes = [[1,0],[2,2],[2,1]]
Output: 
[0,2,1]
Explanation: 
Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].


My solution:










https://zhongwen.gitbook.io/leetcode-report/medium/1057.-campus-bikes
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        distances = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, i, j))
        distances.sort()
        
        eleset = set()
        res = [-1] * len(workers)
        for d, w, b in distances:
            if res[w] == -1 and b not in eleset:
                res[w] = b
                eleset.add(b)
        return res
