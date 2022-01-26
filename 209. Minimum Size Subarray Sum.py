Question:
Given an array of positive integers nums and a positive integer target, return the minimal length of 
a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal 
to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.


Solution: sliding window

Similar to 862. Shortest Subarray with Sum at Least K
The result is initialized as res = n + 1. One pass, remove the value from sum s by doing s -= A[j]. 
If s <= 0, it means the total sum of A[i] + ... + A[j] >= sum that we want. 
Then we update the res = min(res, j - i + 1). Finally we return the result res

    def minSubArrayLen(self, s, A):
        i, res = 0, len(A) + 1
        for j in xrange(len(A)):
            s -= A[j]
            while s <= 0:
                res = min(res, j - i + 1)
                s += A[i]
                i += 1
        return res % (len(A) + 1)

Complexity
Time O(N)
Space O(1)


Similar Sliding window:

1248. Count Number of Nice Subarrays
1234. Replace the Substring for Balanced String
1004. Max Consecutive Ones III
930. Binary Subarrays With Sum
992. Subarrays with K Different Integers
904. Fruit Into Baskets
862. Shortest Subarray with Sum at Least K



