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

        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in xrange(l)] for _ in xrange(m)]
        for i in xrange(m):
            for k in xrange(n):
                if A[i][k]:
                    for j in xrange(l):
                        res[i][j] += A[i][k] * B[k][j]
        return res

    
    
# Time:  O(m * n * l), A is m x n matrix, B is n x l matrix
# Space: O(m * l)    
