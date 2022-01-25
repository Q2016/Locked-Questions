Question:
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the 
i-th employee, manager[headID] = -1. The head of the company wants to inform all the company employees of an 
urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until 
all employees know about the urgent news. The i-th employee needs informTime[i] minutes to inform all of his 
direct subordinates. Return the number of minutes needed to inform all the employees about the urgent news.

Example 1:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and 
needs 1 minute to inform them all.


Solution:  Dijkstra or DFS or BFS


Dijkstra
Just look at this as a network problem. We are trying to find the bottleneck of the network.
Treat the managers and employees as the nodes and the inform time as the weight of the edges.

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for i, managerId in enumerate(manager):
            graph[managerId].append((informTime[i], i))
        
        dist = {}
        heap = [(informTime[headID], headID)] 
        
        while heap:
            time, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = time    
            for w, v in graph[u]:
                if v in dist:
                    continue
                heapq.heappush(heap, (time+w, v))    
        return max(dist.values()) 

DFS
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = collections.defaultdict(list)
        self.res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
        
        def dfs(manager, time):
            self.res = max(self.res, time)
            for subordinate in subordinates[manager]:
                dfs(subordinate, time + informTime[manager])
        dfs(headID, 0)        
        return self.res

    
    
BFS
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = collections.deque([(headID, 0)])
        subordinates = collections.defaultdict(list)
        res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
            
        while q:
            u, time = q.popleft()
            res = max(res, time)
            for v in subordinates[u]:
                q.append((v, time + informTime[u]))
        return res
