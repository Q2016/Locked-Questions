Question:
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less 
than or equal to threshold or return 0 if there is no such square.

Example 1:
Input: mat = [[|1,1|,3,2,4,3,2],
              [|1,1|,3,2,4,3,2],
              [1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
    
    
    
Solution: Prefix sum

PrefixSum prefixsum[i][j] is the sum of every element from (0,0) to (i,j).
By using prefix sum, we can calculate the sum of every element from (i,j) to (i+k,j+k) easily.
sum = prefixSum[i+k][j+k] - prefixSum[i-1][j+k] - prefixSum[i+k][j-1] + prefixSum[i-1][j-1]

Time: O(m*n*Min(m,n))

class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length, n = mat[0].length;
        // Find prefix sum
        int[][] prefixSum = new int[m+1][n+1];
        for (int i = 1; i <= m; i++) {
            int sum = 0;
            for (int j = 1; j <= n; j++) {
                sum += mat[i-1][j-1];
                prefixSum[i][j] = prefixSum[i-1][j] + sum;
            }
        }
        // Start from the largest side length
        for(int k = Math.min(m, n)-1; k > 0; k--) {
            for(int i = 1; i+k <= m; i++) {
                for(int j = 1; j+k <= n; j++) {
                    if(prefixSum[i+k][j+k] - prefixSum[i-1][j+k] - prefixSum[i+k][j-1] + prefixSum[i-1][j-1] <= threshold) {
                        return k+1;
                    }
                }
            }
        }
        return 0;
    }
}
