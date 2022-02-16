Question:
You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]    

    
Solution:
If b is a subset of a, then say a is a superset of b. Also, say N_"a"(word) is the count of the number of "a"'s in the word.
When we check whether a word wordA in A is a superset of wordB, we are individually checking the counts of letters: that 
for each letter, we have N_letter(wordA) => N_letter(wordB)
Now, if we check whether a word wordA is a superset of all words wordB_i, we will check for each letter and each ii, that N_letter(wordA) => N_letter(wordB_i). 
This is the same as checking N_letter(wordA) => max N_letter(wordB_i) 
For example, when checking whether "warrior" is a superset of words B = ["wrr", "wa", "or"], we can combine these words in B to form a 
"maximum" word "arrow", that has the maximum count of every letter in each word in B.
Reduce B to a single word bmax as described above, then compare the counts of letters between words a in A, and bmax.    

class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
