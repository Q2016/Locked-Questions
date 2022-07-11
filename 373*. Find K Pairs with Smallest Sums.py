Question:
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k. Define a pair (u, v) which consists of 
one element from the first array and one element from the second array. Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with 
the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


		
		
		
		
	
	
	
	
	
	
	
	
	
Basic Brute-Force is to create a 2D of sum of pairs and pushing into priority Queue and pop() kth smallest		
		
Solution: priority Queue
	
It's helpful to visualize the input as an m×n matrix of sums, for example for nums1=[1,7,11], and nums2=[2,4,6]:
      2   4   6
   +------------
 1 |  3   5   7
 7 |  9  11  13
11 | 13  15  17

Creating the matrix now it's 378. Kth Smallest Element in a Sorted Matrix problem.

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/209985/python-heap-solution-with-detail-explanation
	
	
from heapq import *
class Solution:

    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2:
            return []

        visited = []
        heap = []
        output = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.append((0, 0))

        while len(output) < k and heap:

            val = heappop(heap)
            output.append((nums1[val[1]], nums2[val[2]]))

            if val[1] + 1 < len(nums1) and (val[1] + 1, val[2]) not in visited:
                heappush(heap, (nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]))
                visited.append((val[1] + 1, val[2]))

            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heappush(heap, (nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1))
                visited.append((val[1], val[2] + 1))

        return output
