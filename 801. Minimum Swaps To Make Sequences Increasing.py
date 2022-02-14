Question:
You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].
For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the 
given input always makes it possible.
An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

Example 1:
Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
Output: 1
Explanation: 
Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
which are both strictly increasing.



Solution:
swap[n] means the minimum swaps to make the A[i] and B[i] sequences increasing for 0 <= i <= n,
in condition that we swap A[n] and B[n]
not_swap[n] is the same with A[n] and B[n] not swapped.

@Acker help explain:

A[i - 1] < A[i] && B[i - 1] < B[i].
In this case, if we want to keep A and B increasing before the index i, can only have two choices.
-> 1.1 don't swap at (i-1) and don't swap at i, we can get not_swap[i] = not_swap[i-1]
-> 1.2 swap at (i-1) and swap at i, we can get swap[i] = swap[i-1]+1
if swap at (i-1) and do not swap at i, we can not guarantee A and B increasing.

A[i-1] < B[i] && B[i-1] < A[i]
In this case, if we want to keep A and B increasing before the index i, can only have two choices.
-> 2.1 swap at (i-1) and do not swap at i, we can get notswap[i] = Math.min(swap[i-1], notswap[i] )
-> 2.2 do not swap at (i-1) and swap at i, we can get swap[i]=Math.min(notswap[i-1]+1, swap[i])


Complexty
Time O(N)
Space O(N)

    def minSwap(self, A, B):
        N = len(A)
        not_swap, swap = [N] * N, [N] * N
        not_swap[0], swap[0] = 0, 1
        for i in range(1, N):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap[i] = swap[i - 1] + 1
                not_swap[i] = not_swap[i - 1]
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                swap[i] = min(swap[i], not_swap[i - 1] + 1)
                not_swap[i] = min(not_swap[i], swap[i - 1])
        return min(swap[-1], not_swap[-1])
  
  
Complexty
Time O(N)
Space O(1)       
        
        
    def minSwap(self, A, B):
        N = len(A)
        not_swap, swap = 0, 1
        for i in range(1, N):
            not_swap2 = swap2 = N
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap2 = swap + 1
                not_swap2 = not_swap
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                swap2 = min(swap2, not_swap + 1)
                not_swap2 = min(not_swap2, swap)
            swap, not_swap = swap2, not_swap2
        return min(swap, not_swap) 
   
   
   
 
        
        
