Question:
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:
Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.


Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.    
    

    
Solution:    


Complexity
Time O(N) for one pass
Space O(2) for two options


    def movesToMakeZigzag(self, A):
        A = [float('inf')] + A + [float('inf')]
        res = [0, 0]
        for i in xrange(1, len(A) - 1):
            res[i % 2] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)
        return min(res)
