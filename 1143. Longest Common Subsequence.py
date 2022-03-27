Question:
Given two strings text1 and text2, return the length of their longest common subsequence. 
A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"  Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.    
    
    
    
    
    
    
Solution: DP

If the two strings have no matching characters, so the last line always gets executed, the the time bounds are binomial coefficients, 
which (if m=n) are close to 2^n.

							lcs("AXYT", "AYZX")
                           /              \
             lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
             /        \                      /              \ 
    lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")

            
    class Solution:
        def longestCommonSubsequence(self, s1: str, s2: str) -> int:
            return self.helper(s1, s2, 0, 0)
            
        def helper(self, s1, s2, i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + self.helper(s1, s2, i + 1, j + 1)
            else:
                return max(self.helper(s1, s2, i+1, j), self.helper(s1, s2, i, j + 1))

            
 Recursive solution with Memoization
    
    
    class Solution:
        def longestCommonSubsequence(self, s1: str, s2: str) -> int:
            m = len(s1)
            n = len(s2)
            memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
            return self.helper(s1, s2, 0, 0, memo)
    
        def helper(self, s1, s2, i, j, memo):
            if memo[i][j] < 0:
                if i == len(s1) or j == len(s2):
                    memo[i][j] = 0
                elif s1[i] == s2[j]:
                    memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
                else:
                    memo[i][j] = max(self.helper(s1, s2, i + 1, j, memo), self.helper(s1, s2, i, j + 1, memo))
            return memo[i][j]
        
Time analysis: each call to subproblem takes constant time. We call it once from the main routine, and at most twice every 
time we fill in an entry of array L. There are (m+1)(n+1) entries, so the total number of calls is at most 2(m+1)(n+1)+1 and the time is O(mn).
As usual, this is a worst case analysis. The time might sometimes better, if not all array entries get filled out. For instance if the 
two strings match exactly, we'll only fill in diagonal entries and the algorithm will be fast.
            
            
            
LCS is a well-known problem, and there are similar problems here:
1092. Shortest Common Supersequence
1062. Longest Repeating Substring
516. Longest Palindromic Subsequence
1312. Minimum Insertion Steps to Make a String Palindrome
