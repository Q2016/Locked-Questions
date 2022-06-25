Question:
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: grid = [[0,0,0,0],
               [1,0,1,0],
               [0,1,1,0],
               [0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.    

  
  
  
  
  
  
  
  
Intuition:
DFS Solution using flood-fill
The first cycle does DFS for the boundary cells. flood the 1's at boundary with 0 
The second cycle counts the remaining land.

Solution: DFS

class Solution {
    public:
    
    void dfs(vector<vector<int>>& A, int i, int j) {
        if (i < 0 || j < 0 || i == A.size() || j == A[i].size() || A[i][j] != 1) return;
        A[i][j] = 0;
        
        dfs(A, i + 1, j); 
        dfs(A, i - 1, j); 
        dfs(A, i, j + 1); 
        dfs(A, i, j - 1);
    }
    
    int numEnclaves(vector<vector<int>>& A) {
        for (auto i = 0; i < A.size(); ++i)
            for (auto j = 0; j < A[0].size(); ++j) 
                if  (i * j == 0 || i == A.size() - 1 || j == A[i].size() - 1) dfs(A, i, j); #flood fills the boundary 

      return accumulate(begin(A), end(A), 0, [](int s, vector<int> &r) # sums the remaining '1's
        { return s + accumulate(begin(r), end(r), 0); });
    }
};



