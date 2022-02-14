Question:
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s. A subsequence of a string is a new 
string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
 
Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".    
    

    
Solution:    
https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/number-of-matching-subsequences.py

class Solution(object):
    def numMatchingSubseq(self, S, words):

        waiting = collections.defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])
