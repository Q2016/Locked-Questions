Question:
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous 
subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. 

Example 1:
Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have 
the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 	


Solution: Prefix sum

Prefix sums have a solid usage in dealing with sub-array sums.Prefix sum array can simply called as cumulative sum array.
Eg: prefixSumArray of [1,4,3] is [1,5,8] i.e [1, 1+4, 1+4+3]
Now that we know prefix sums array is, how to find a sub-array sum with this array?
For [1,4,3] lets see the sub-array sums:
for ease,we can add an extra 0 upfront to the prefix-sums array.=> [0,1,5,8]
If we observe, the difference between elements in the prefixsums array gives the subarray sum of that particular segment of the array. 
5-0 gives the sum of [1,4]
5-1 gives the sum of [4].
8-0 gives the sum of [1,4,3]
8-1 gives sum of [4,3]
8-5 gives sum of [3]


	def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
		ans = []
		prefix = [0]
		for num in nums:
			prefix.append(prefix[-1]+num)

		n = len(prefix)
		for i in range(1,n):
			for j in range(i-1,-1,-1):
				total = prefix[i] - prefix[j]
				ans.append(total)

		ans.sort()
		return sum(ans[left-1:right])

		
Time : O(n^2) | Space:O(n)
		
