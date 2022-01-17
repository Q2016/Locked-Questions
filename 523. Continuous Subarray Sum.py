https://leetcode.com/problems/continuous-subarray-sum/discuss/485589/C%2B%2BPython-Easy-and-Concise


Explanation:
cur calculate the prefix sum remainder of input array A
seen will record the first occurrence of the remainder.
If we have seen the same remainder before,
it means the subarray sum if a multiple of k


Complexity
Time O(N)
Space O(N)


Python:

    def checkSubarraySum(self, A, k):
        seen, cur = {0: -1}, 0
        for i, a in enumerate(A):
            cur = (cur + a) % abs(k) if k else cur + a
            if i - seen.setdefault(cur, i) > 1: return True
        return False
      
      
or:
  
  
  class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = 0
        lookup = {0: -1}
        for i, num in enumerate(nums):
            count += num
            if k:
                count %= k
            if count in lookup:
                if i - lookup[count] > 1:
                    return True
            else:
                lookup[count] = i
        
        return False
