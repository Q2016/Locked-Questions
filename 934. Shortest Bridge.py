Question:
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island. Return the smallest number of 0's you must flip to connect the two islands.    
Example 1:
Input: grid = [[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,1,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1]]
Output: 1    

    
    
    
    
    
    
Solution: DFS+ BFS

For the figure:
    
    https://leetcode.com/problems/shortest-bridge/discuss/189293/C%2B%2B-BFS-Island-Expansion-%2B-UF-Bonus
        
int paint(vector<vector<int>>& A, int i, int j) {
    if (min(i, j) < 0 || max(i, j) == A.size() || A[i][j] != 1)
        return 0;
    A[i][j] = 2;
    return 1 + paint(A, i + 1, j) + paint(A, i - 1, j) + paint(A, i, j + 1) + paint(A, i, j - 1);
}
bool expand(vector<vector<int>>& A, int i, int j, int cl) {
    if (min(i, j) < 0 || max(i, j) == A.size())
        return false;
    A[i][j] = A[i][j] == 0 ? cl + 1 : A[i][j];
    return A[i][j] == 1;
}  
int shortestBridge(vector<vector<int>>& A) {
    for (int i = 0, found = 0; !found && i < A.size(); ++i)
        for (int j = 0; !found && j < A[0].size(); ++j)
            found = paint(A, i, j);
    for (int cl = 2; ; ++cl)
        for (int i = 0; i < A.size(); ++i)
            for (int j = 0; j < A.size(); ++j) 
                if (A[i][j] == cl && ((expand(A, i - 1, j, cl) || expand(A, i, j - 1, cl) || 
                    expand(A, i + 1, j, cl) || expand(A, i, j + 1, cl))))
                        return cl - 2;
}

C++
Same idea, but using a queue instead of scaning the grid.

int dir[5] = {0, 1, 0, -1, 0};
void paint(vector<vector<int>>& A, int i, int j, vector<pair<int, int>> &q) {
    if (min(i, j) >= 0 && max(i, j) < A.size() && A[i][j] == 1) {
        A[i][j] = 2;
        q.push_back({i, j});
        for (int d = 0; d < 4; ++d)
            paint(A, i + dir[d], j + dir[d + 1], q);
    }
}
int shortestBridge(vector<vector<int>>& A) {
    vector<pair<int, int>> q;
    for (int i = 0; q.size() == 0 && i < A.size(); ++i)
        for (int j = 0; q.size() == 0 && j < A[0].size(); ++j)
            paint(A, i, j, q);
    while (!q.empty()) {
        vector<pair<int, int>> q1;
        for (auto [i, j] : q) {
            for (int d = 0; d < 4; ++d) {
                int x = i + dir[d], y = j + dir[d + 1];
                if (min(x, y) >= 0 && max(x, y) < A.size()) {
                    if (A[x][y] == 1)
                        return A[i][j] - 2;
                    if (A[x][y] == 0) {
                        A[x][y] = A[i][j] + 1;
                        q1.push_back({x, y});
                    }
                }
            }
        }
        swap(q, q1);
    }
    return 0;
}        
