Question:
Given an array of integers nums and an integer limit, return the size of the longest non-empty 
subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.    


Solution: BST, Heap, Deques
    
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)
Intuition
Last week we learned, in 1425. Constrained Subsequence Sum how to get minimum in a subarray when sliding.
This week, we need to get both the maximum and the minimum, at the same time.



Solution 1: Binary insert and remove Keep an increasing list L. Binary insert the current element.
If the L[L.size() - 1] - L[0] > limit, binary search the position of A[i] and remove it from the list.

Time O(N^2)
Space O(N)

    def longestSubarray(self, A, limit):
        i, L = 0, []
        for j in xrange(len(A)):
            bisect.insort(L, A[j])
            if L[-1] - L[0] > limit:
                L.pop(bisect.bisect(L, A[i]) - 1)
                i += 1
        return j - i + 1

Solution 2: Use two heaps
Time O(NogN)
Space O(N)

    def longestSubarray(self, A, limit):
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i: heapq.heappop(maxq)
                while minq[0][1] < i: heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res

Solution 3: Use two deques
Time O(N)
Space O(N)

    def longestSubarray(self, A, limit):
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in A:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
        return len(A) - i

    
    
    
    
    
    
More Similar Sliding Window Problems:

Constrained Subsequence Sum
Number of Substrings Containing All Three Characters
Count Number of Nice Subarrays
Replace the Substring for Balanced String
Max Consecutive Ones III
Binary Subarrays With Sum
Subarrays with K Different Integers
Fruit Into Baskets
Shortest Subarray with Sum at Least K
Minimum Size Subarray Sum


More Good Stack Problems:

Constrained Subsequence Sum
Minimum Cost Tree From Leaf Values
Sum of Subarray Minimums
Online Stock Span
Score of Parentheses
Next Greater Element II
Next Greater Element I
Largest Rectangle in Histogram
Trapping Rain Water

