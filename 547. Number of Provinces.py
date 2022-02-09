Question:
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly 
connected, and isConnected[i][j] = 0 otherwise. Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],                 1-------2
		      [1,1,0],                     3
Output: 2             [0,0,1]]
	
	
Solution: DFS or BFS
class Solution:
    # The main function is exactaly the same with BFS
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [False] * len(M)
        res = 0
        for student in range(len(M)):
            if not visited[student]:
                res += 1 # We only increment the count of friend circle on an unvisited root
                visited[student] = True
                self.visitAllFriends(student, M, visited)
        return res

    # This helper function's job is only to mark all direct & indirect friends as visited
    # (not increment count at all since we've counted the root already) 
    def visitAllFriends(self, student, M, visited):
        for s, r in enumerate(M[student]):
            if r == 1 and visited[s] == False:
                visited[s] = True
                self.visitAllFriends(s, M, visited)
# BFS 
class Solution:
    # The main function is exactaly the same with DFS
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [False] * len(M)
        res = 0
        for student in range(len(M)):
            if not visited[student]:
                res += 1
                visited[student] = True
                self.visitAllFriends(student, M, visited)
        return res
     
    # This helper function share the same job with DFS
    def visitAllFriends(self, student, M, visited):
        queue = []
        queue.append(student)
        while queue:
            tempStudent = queue.pop(0)
            visited[tempStudent] = True
            for s, r in enumerate(M[tempStudent]):
                if r == 1 and visited[s] == False:
                    queue.append(s)

