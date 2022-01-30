Question:
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon 
subsequence does not exist, return -1. An uncommon subsequence between an array of strings is a string that is a subsequence 
of one string but not the others. A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". 
Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

Example 1:
Input: strs = ["aba","cdc","eae"]
Output: 3

    
Solution:    
https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/99453/Python-Simple-Explanation

When we add a letter Y to our candidate longest uncommon subsequence answer of X, it only makes it strictly harder to find a 
common subsequence. Thus our candidate longest uncommon subsequences will be chosen from the group of words itself.
Suppose we have some candidate X. We only need to check whether X is not a subsequence of any of the other words Y. 
To save some time, we could have quickly ruled out Y when len(Y) < len(X), either by adding "if len(w1) > len(w2): return False" 
or enumerating over A[:i] (and checking neighbors for equality.) However, the problem has such small input constraints that this is not required.
We want the max length of all candidates with the desired property, so we check candidates in descending order of length. 
When we find a suitable one, we know it must be the best global answer.

    def subseq(w1, w2):
        #True iff word1 is a subsequence of word2.
        i = 0
        for c in w2:
            if i < len(w1) and w1[i] == c:
                i += 1
        return i == len(w1)

    A.sort(key = len, reverse = True)
    for i, word1 in enumerate(A):
        if all(not subseq(word1, word2) 
                for j, word2 in enumerate(A) if i != j):
            return len(word1)
    return -1


