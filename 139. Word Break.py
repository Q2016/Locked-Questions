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
    
    
C++:    
    
class Solution {
    bool wordBreak(string s, unordered_set<string>& wordDict) {
        return canBrk(0,s,wordDict);    
    }
    bool canBrk(int start, string& s, unordered_set<string>& wordDict) {
        int n = s.size();
        if(start == n) return 1;
        string sub;
        for(int i = start; i<n; i++) if(wordDict.count(sub+=s[i]) && canBrk(i+1,s,wordDict)) return 1;
        return 0;
    }   
     
    
Getting rid of TLE

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<int> memo(s.size(), -1);
        return check(s, wordSet, 0, memo);
    }
    bool check(string s, unordered_set<string>& wordSet, int start, vector<int>& memo) {
        if (start >= s.size()) 
            return true;
        if (memo[start] != -1) 
            return memo[start];
        for (int i = start + 1; i <= s.size(); ++i) {
            if (wordSet.count(s.substr(start, i - start)) && check(s, wordSet, i, memo)) {
                memo[start] = 1;
                return memo[start];
            }
        }
        memo[start] = 0;
        return memo[start];
    }
};
