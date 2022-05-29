Question:
Given two sparse matrices A and B, return the result of AB. You may assume that A's column number is equal to B's row number.

Example:
A = [[ 1, 0, 0],        B = [[ 7, 0, 0 ],
     [-1, 0, 3]]             [ 0, 0, 0 ],
                             [ 0, 0, 1 ]]

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |    

     
     
     
     
     
     
     
     
     
     
Solution:    

    def multiply(self, A, B):

        m, n, nB = len(A), len(A[0]), len(B[0])
        res = [[0]* nB for _ in range(m)]
        
          
          for i in range(m):
              for j in range(nB):
                    res[i][j] = sum(A[i][k] * B[k][j])
                    
        return res

    
    
# Time:  O(m * n * nB), A is m x n matrix, B is n x nB matrix
# Space: O(m * nB)    
