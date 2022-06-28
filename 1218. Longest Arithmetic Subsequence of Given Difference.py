Question:
Given an integer array and an integer difference, return the length of the longest 
subsequence in arr which is an arithmetic sequence such that the difference between adjacent 
elements in the subsequence equals difference.
A subsequence is a sequence that can be derived from arr by deleting some or no elements without 
changing the order of the remaining elements.

Example 1:
Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].        

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].        
        
        
        

        
        
        
        
        
Longest subsequence is a DP problem        
        
Solution:  
        
        
        
        
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n=len(arr)
        
        dp={} # dp[i]: what's the length of subsequence ending in 'i'
        ans=0
        
        for num in arr:
           target=num-difference
           if target not in dp: # search in the keys like 2sum
              dp[num]=1
           else:
              dp[num]=1+dp[target] # dp[i]=1+dp[i-diff] wich makes sense
        
           ans=max(ans, dp[num])

        return ans
