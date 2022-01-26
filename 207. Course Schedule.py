Question:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take 
course bi first if you want to take course ai.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.    


Solution: Toplogical Sort

Easiest way (for me) to remember topsort is white/grey/black. If a node is white then it can be visited, 
if it's grey it's being visited and if it's black then it's been visited. If we encouter a black node 
while we're traversing then great we know it's all good, if we encounter a grey node then we have hit a 
cycle and we should just throw an exception or something and if we encounter a white node then it needs 
to be explored. I've opted to raise an exception when we hit a grey node and rely on that as that's what 
you'd expect to see in the real world, but you could also set a global (or class-level) variable all the same.

WHITE = 0
GREY = 1
BLACK = 2

class Solution:
    def topsort(self, adj_list, node, state, results):
        if state[node] == GREY:
            raise Exception('Cycle detected')
        elif state[node] == BLACK:
            return
        state[node] = GREY
        if node in adj_list:
            for neighbor in adj_list[node]:
                self.topsort(adj_list, neighbor, state, results)
        results.append(node)
        state[node] = BLACK
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = dict()
        for prereq in prerequisites:
            if prereq[0] not in adj_list:
                adj_list[prereq[0]] = []
            adj_list[prereq[0]].append(prereq[1])
        state = [WHITE for _ in range(numCourses)]
        results = []
        for i in range(numCourses):
            try:
                self.topsort(adj_list, i, state, results)
            except:
                return False
        return True    
    
