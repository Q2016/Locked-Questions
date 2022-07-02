Question:
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]    


    
    
    
    
    
    
Solution: Recursive (Interesting)
(Initially, I thought backtracking but it's not clear how many choices we have at each node)

Find answer recursively and memory trick can save some time
traverse and check every prefix s[:i] of s
if prefix s[:i] is a palindrome, then process the left suffix s[i:] recursively
since the suffix s[i:] may repeat, the memory trick can save some time
image

Time  Complexity: O(N * (2 ^ N))
Space Complexity: O(N * (2 ^ N))
Python3

class Solution(object):
    @cache  # the memory trick can save some time
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
Python

class Solution(object):
    def __init__(self):
        self.memory = collections.defaultdict(list)
        
    def partition(self, s):
        if not s: return [[]]
        if s in self.memory: return self.memory[s]  # the memory trick can save some time
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        self.memory[s] = ans
        return ans
