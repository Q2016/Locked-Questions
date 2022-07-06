Question:
Given an integer n, return the least number of perfect square numbers that sum to n. A perfect square is an integer that 
is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 
are perfect squares while 3 and 11 are not.    











If think, you will realize that starting from n picking the first i^2 wont work because no garaunty all will sum to n. So here seems like a backtracking
and since we can reduce the problem to sub problems it's dynamical programming.

Solution : Dynamic Programming

    https://www.youtube.com/watch?v=HLZLwjzIVGo
    
Time complexity O(N*sqrt(N))    
    
class Solution 

    def numSquares(self, n):
        dp=[n]*(n+1)
        dp[0]=0
        
        for target in range(1, n+1):
            for s in range(1, target+1):
                square=s*s
                if target -square<0:
                    break
                dp[target]=min(dp[target],1+dp[target-square])
                
        return dp[n]
