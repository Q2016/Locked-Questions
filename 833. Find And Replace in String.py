Question:
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed 
parallel arrays, indices, sources, and targets, all of length k.
To complete the ith replacement operation:
Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".
All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The 
testcases will be generated such that the replacements will not overlap.
For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".




Solution
https://leetcode.com/problems/find-and-replace-in-string/discuss/130587/C%2B%2BJavaPython-Replace-S-from-right-to-left

Intuition:
Verify equality of string and change it if necessay.
The only thing we need take attention is that the string form sources and targets can be different.
Instead of record the length changement, I sort indexes and do it from right to left.
(Since indexes.length <= 100 is really small)
In this way, the different length won't bother us anymore.


Explanation:
Descending indexes[] with tracking its index.
Verify equality of subring in S source and source.
Replace S if necessay.

Time Complexity:
O(SN)

Comments from @CanDong:
Since there won't be any overlap in replacement,
every character in S will be compared at most once.
If using StringBuilder, it should be O(NlogN + S).



    def findReplaceString(self, S, indexes, sources, targets):
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
        return S
