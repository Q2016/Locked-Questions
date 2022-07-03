Question:
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
 
Example1:
s = "leetcode",
dict = ["leet", "code"]. 
Return true because "leetcode" can be segmented as "leet code".









Solution: 
For understanding time complexity:
https://leetcode.com/problems/word-break/discuss/169383/solved-The-Time-Complexity-of-The-Brute-Force-Method-Should-Be-O(2n)-and-Prove-It-Below
    
Recursion, Average O(2^n)
T(n) = T(n-1)+T(n-2)+...+T(1)
=> T(n+1) = T(n)+T(n-1)+T(n-2)+...+T(1)
=>T(n+1) = 2T(n)
    
Python:
    
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)
   
        @lru_cache(None)
        def dfs(k):
            if k == n: return True
            for i in range(k + 1, n + 1):
                if s[k:i] in wordSet and dfs(i):
                    return True        
            return False
        
        return dfs(0)    
    
    
Class Solution:
 
def wordBreak(self, s, wordDict):
  dp=[False]*(len(s)+1)
  dp[len(s)]=True
  
  for i in range(len(s)-1,-1,-1):
    for w in wordDict:
      if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
        dp[i]=dp[i+len(w)]
        
      if dp[i]:
        break
        
  return dp[0]
    
    
    
