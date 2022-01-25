Question:
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:
Input: nums = [[1,2,3],
	       [4,5,6],
	       [7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]	
	
	
Solution: Dictionary	

https://leetcode.com/problems/diagonal-traverse-ii/discuss/597980/Python-Two-simple-solutions-(dictionary-or-sort)-O(n)

The first solution is to use dictionary. Complexity O(n)
Record the (r+c) as the key, then reverse list for each (r+c) and append it to the result.


	def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
		D = collections.defaultdict(list)
		R = len(nums)

		for r in range(R):
			for c in range(len(nums[r])):
				D[r+c].append(nums[r][c])

		res = []
		for k in sorted(D.keys()):
			res.extend(D[k][::-1])
		return res
