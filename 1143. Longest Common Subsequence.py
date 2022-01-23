Question:
Given two strings text1 and text2, return the length of their longest common subsequence. 
A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.    
    
    
    
Solution: DP

//https://en.m.wikipedia.org/wiki/Longest_common_subsequence_problem    

class Solution {
public:
    int longestCommonSubsequence(string a, string b) {
    vector<vector<short>> m(a.size() + 1, vector<short>(b.size() + 1));
  
    for (auto i = 1; i <= a.size(); ++i)
        for (auto j = 1; j <= b.size(); ++j)
            if (a[i - 1] == b[j - 1]) 
                m[i][j] = m[i - 1][j - 1] + 1;
            else 
                m[i][j] = max(m[i - 1][j], m[i][j - 1]);
  
    return m[a.size()][b.size()];
    }
};
