Question:
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 4    


    
solution: DP


    def maximalSquare(self, M):
        def is_valid_sqaure(row, col, side):
            return all(all(M[i][j] == '1' for j in range(col, col+side)) for i in range(row, row+side))
        m, n = len(M), len(M[0])
        for side_len in range(min(m,n), 0, -1):
            for row in range(m - side_len + 1):
                for col in range(n - side_len + 1):
                    if is_valid_sqaure(row, col, side_len):
                        return side_len**2
        return 0
    
    
Time Complexity : O(M*N*min(M,N)3)
Space Complexity : O(1), only constant extra space is being used
