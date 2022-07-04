Question:
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous 
subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. 

Example 1:
Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have 
the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 	














Solution: 

Approach 1 (brute force)
Collect all "range sum" and sort them. Return the sum of numbers between left and right modulo 1_000_000_007.

O(N^2 logN) time & O(N^2) space (376ms)

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for i in range(len(nums)):
            prefix = 0
            for ii in range(i, len(nums)):
                prefix += nums[ii]
                ans.append(prefix)
        ans.sort()
        return sum(ans[left-1:right]) % 1_000_000_007
		
