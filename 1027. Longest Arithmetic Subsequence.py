Question:
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] 
with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic if 
seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

 

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.  






Solution: DP, similar to LIS (Longest Increasing Subsequence) problem   

in the comments of
https://leetcode.com/problems/longest-arithmetic-subsequence/discuss/274584/Same-as-LIS-problem-python-solution
  

d[i][v] means the length ending with A[i] for a difference v

    def longestArithSeqLength(self, A: List[int]) -> int:
        d = collections.defaultdict(dict)
        n = len(A)
        res = 1
        for i in range(n):
            for j in range(i):
                v = A[i] - A[j]
                # the default length is 1
                if v not in d[j]: d[j][v] = 1
                if v not in d[i]: d[i][v] = 0
                d[i][v] = max(d[i][v] ,d[j][v] + 1) # i dont understand the '1'
                res = max(res, d[i][v])
        return res
