Question:
Given a list of strings 'words' and a string 'pattern', return a list of 'words[i]' that match 'pattern'. You may return the answer in any order.
A word matches the pattern if there exists a permutation of letters 'p' so that after replacing every letter 'x' in the pattern with 'p(x)', we 
get the desired word.

Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.








Solution: Two Maps (The code is clear)


class Solution(object):
    
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)
