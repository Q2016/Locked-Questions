class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        if (M.empty()) return 0;
        int n = M.size();
        vector<bool> visited(n, false);
        int groups = 0;
        for (int i = 0; i < visited.size(); i++) {
            groups += !visited[i] ? dfs(i, M, visited), 1 : 0;
        }
        return groups;
    }

private:
    void dfs(int i, vector<vector<int>>& M, vector<bool>& visited) {
        visited[i] = true;
        for (int j = 0; j < visited.size(); j++) {
            if (i != j && M[i][j] && !visited[j]) {
                dfs(j, M, visited);
            }
        }
    }
};

/*
The following DFS and BFS algorithm share the same main function findCircleNum() (exactly the same!). The only difference between them is the helper function visitAllFriends(). DFS uses recursion while BFS uses a queue to mark direct & indirect friends as visited.

I wrote with minimum difference for myself to compare and understand the major difference. Hope it helps!

# DFS
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
*/
