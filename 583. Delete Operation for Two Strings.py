Question:
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".    

    
    
    
    
    
    
    
    
    
Solution:
Find the longest common subsequence (LCS). Number of deletions will be : (word1.length - LCS) + (word2.length - LCS)

    def minDistance(word1, word2):
        m = len(word1)
        n = len(word2)
        #dp[m+1][n+1];    
        for i in range(m+1):    # LCS for "XXXXXX" and "" will be 0
            dp[i][0] = 0;
        for j in range(n+1):    # LCS for "" and "XXXXX" will be 0
            dp[0][j] = 0;
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (word1[i-1] == word2[j-1]):        
                  dp[i][j] = dp[i-1][j-1] + 1;
              else: 
                  dp[i][j] = max(dp[i-1][j],dp[i][j-1]);  
        return m - dp[m][n] + n - dp[m][n];
    
