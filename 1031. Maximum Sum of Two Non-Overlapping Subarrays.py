https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/discuss/581060/Python-prefix-sum-with-diagram-explanation

refer above for the figure, it's also related to buy/sell stocks III


Solution: prefix sum with diagram explanation


Explanation: Suppose we already have array of prefix sum, and we are at index i-th of prefix_sum. There are two possible ways to find maximum result:
(1) maxL + the last sum of A's subarray of length == M. maxL:= maximum sum of A's subarray of length == L, before the ending at i, and the last subarray with length == M. (In the diagram, possible result (1))

(2) maxM + the last sum of A's subarray of length == L. maxM:= maximum sum of A's subarray of length == M, before the ending at i, and the last subarray with length == L. (In the diagram, possible result (2))

Complexity: Time O(N), N is len(A). Space O(1)

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if len(A) < L + M: return 0
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        res, maxL, maxM = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, len(A)):
            maxL = max(maxL, A[i - M] - A[i - M - L])
            maxM = max(maxM, A[i - L] - A[i - L - M])
            res = max(res, maxL + A[i] - A[i - M], maxM + A[i] - A[i - L])
        return res
