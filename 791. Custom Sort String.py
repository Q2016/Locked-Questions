Question:
You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously. Permute the characters of s 
so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur 
before y in the permuted string. Return any permutation of s that satisfies this property.

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.  









Solution:
Similar to 1122. Relative Sort Array

    def customSortString(self, S: str, T: str) -> str:
        ans, cnt = [], collections.Counter(T)           # count each char in T. 
        for c in S:
            if cnt[c]: ans.extend(c * cnt.pop(c))       # sort chars both in T and S by the order of S.
        for c, v in cnt.items():
            ans.extend(c * v)                           # group chars in T but not in S.
        return ''.join(ans);
