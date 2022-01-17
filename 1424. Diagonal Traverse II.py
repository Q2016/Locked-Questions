https://leetcode.com/problems/diagonal-traverse-ii/discuss/597980/Python-Two-simple-solutions-(dictionary-or-sort)-O(n)


The first solution is to use dictionary. Complexity O(n)
Record the (r+c) as the key, then reverse list for each (r+c) and append it to the result.

class Solution:
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
