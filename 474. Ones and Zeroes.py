Question:
You are given an array of binary strings strs and two integers m and n. Return the size of the largest subset of strs 
such that there are at most m 0's and n 1's in the subset. A set x is a subset of a set y if all elements of x are also 
elements of y.

Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.    








Solution: 2D Knapsack Problem

This problem is a variation on the 0-1 Knapsack Problem with a wrinkle: each item has a 2-dimensional weight, 
but a constant value. If we were to naively attempt every single permutation of up to 600 strings, that 
would be 2^600 permutations.

For our DP array (dp), dp[i][j] will represent the largest number of items that can be added to yield i zeros and j ones. 
Thus, our answer will ultimately be dp[M][N]. We'll naturally being doing a bottom-up DP approach, as we'll be starting 
with no data and iterating through the input array (S), adding more data to dp as we go.

For each string, some number of 0s(lets call zeros) and 1s (lets call ones) are required. Obviously, if our balance of zeros and ones is less 
than what is required by current string, we can't choose it. But in the case where our balance of zeros and ones is greater than the required, 
we have two cases -

Either take the current string into our subset. The resultant count would be 1 + optimal solution that we had when our balance was i - zeros & j - ones.
Or leave the current string meaning the resultant count will remain the same.


    def findMaxForm(self, S: List[str], M: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for str in S:
            zeros = str.count("0")
            ones = len(str) - zeros
            for i in range(M, zeros - 1, -1):
                for j in range(N, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[M][N]
    
    
Time Complexity : O(L*M*N), where L is the length of strs
Space Complexity : O(M*N)    
