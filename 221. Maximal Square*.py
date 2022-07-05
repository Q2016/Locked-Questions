Question:
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 4    

  
  
  
  
  
  
  
  

    
solution: DP

We will explain this approach with the help of an example.
0 1 1 1 0
1 1 1 1 1
0 1 1 1 1
0 1 1 1 1
0 0 1 1 1
We initialize another matrix (dp) with the same dimensions as the original one initialized with all 0’s.
dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.
Starting from index (0,0), for every 1 found in the original matrix, we update the value of the current element as
dp(i, j) = min( dp(i-1, j), dp(i-1, j-1), dp(i, j-1) ) + 1
We also remember the size of the largest square found so far. In this way, we traverse the original matrix once and find out the 
required maximum size. 


class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if(matrix.size()==0) return 0;
        int maxSq=0;
        int nRow=matrix.size();
        int nCol=matrix[0].size();
        vector<vector<int>> dp(nRow+1,vector<int>(nCol+1,0));
        #dp[i][j] represents max square ending at position (i-1, j-1)
        for(int i=1;i<=nRow;++i){
            for(int j=1;j<=nCol;++j){
                if(matrix[i-1][j-1]=='1'){
                    dp[i][j]=min({dp[i-1][j-1],dp[i-1][j],dp[i][j-1]})+1;
                    maxSq=max(maxSq,dp[i][j]);
                }
            }
        }
        return maxSq*maxSq;
    }
};

Time complexity : O(mn). Single pass.
Space complexity : O(mn). Another matrix of same size is used for dp.
    

