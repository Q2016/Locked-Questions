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
  


    def longestArithSeqLength(self, A):
        d = [collections.defaultdict(int) for _ in A]
        res = 1
        for i in range(0,len(A)):
            for j in range(i):
                v = A[i]-A[j]
                d[i][v]=max(d[j][v]+1,d[i][v])
                res = max(d[i][v],res)
        return res+1
