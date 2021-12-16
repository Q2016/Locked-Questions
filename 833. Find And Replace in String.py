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
