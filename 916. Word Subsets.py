Question:
You are given two string arrays words1 and words2.
A string 'b' is a subset of string 'a' if every letter in 'b' occurs in 'a' including multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string 'a' from 'words1' is universal if for every string b in 'words2', b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]    

    
    
    
    
    
    
    
    
Solution: Counter
    
The idea here is to use counters: we need to find elements from A, for which each string from B have less or equal frequencies for each symbol. 
Let us create cnt: counter, with maximal values for each letter, that is if we have B = [abb, bcc], then we have cnt = {a:1, b:2 ,c:2}. In python 
it can be written using | symbol.

Second step is for each string a from A calcuate counter and check that it is bigger for each element than cnt. Again in python it can be don in 
very short way, using not cnt - Counter(a).

Complexity: 
time complexity is O(m + n), where m is total length of words in A and m is total length of words in B. 
Space complexity is O(m), because potentially answer can consist all strings from A.

class Solution:
    def wordSubsets(self, A, B):
        cnt = Counter()
        for b in B:
            cnt |= Counter(b)
            
        return [a for a in A if not cnt - Counter(a)]
