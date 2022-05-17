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
    
state
whether we swap the element at index i to make A[0..i] and B[0..i] both increasing can uniquely identify a state, i.e. a node in the state graph.
state function
state(i, 0) is the minimum swaps to make A[0..i] and B[0..i] both increasing if we donot swap A[i] with B[i]
state(i, 1) is the minimum swaps to make A[0..i] and B[0..i] both increasing if we do swap A[i] with B[i]
goal state
min{state(n - 1, 0), state(n - 1, 1)} where n = A.length
state transition
We define areBothSelfIncreasing: A[i - 1] < A[i] && B[i - 1] < B[i], areInterchangeIncreasing: A[i - 1] < B[i] && B[i - 1] < A[i].
Since 'the given input always makes it possible', at least one of the two conditions above should be satisfied.

if i == 0, 
	        state(0, 0) = 0; 
	        state(0, 1) = 1;
			
Generally speaking,
	if areBothSelfIncreasing && areInterchangeIncreasing
	        // Doesn't matter whether the previous is swapped or not.
	        state(i, 0) = Math.min(state(i - 1, 0), state(i - 1, 1));
	        state(i, 1) = Math.min(state(i - 1, 0), state(i - 1, 1)) + 1;
	else if areBothSelfIncreasing
	        // Following the previous action.
	        state(i, 0) =  state(i - 1, 0);
	        state(i, 1) =  state(i - 1, 1) + 1;
	else if areInterchangeIncreasing
	        // Opposite to the previous action.
	        state(i, 0) = state(i - 1, 1);
	        state(i, 1) = state(i - 1, 0) + 1;
        
        
The complete code:          
        
        
    public int minSwap(int[] A, int[] B) {
        int n = A.length;
        int[][] state = new int[n][2];
        state[0][1] = 1;
        
        for (int i = 1; i < n; i++) {
            boolean areBothSelfIncreasing = A[i - 1] < A[i] && B[i - 1] < B[i];
            boolean areInterchangeIncreasing = A[i - 1] < B[i] && B[i - 1] < A[i];
            
            if (areBothSelfIncreasing && areInterchangeIncreasing) {
                state[i][0] = Math.min(state[i - 1][0], state[i - 1][1]);
                state[i][1] = Math.min(state[i - 1][0], state[i - 1][1]) + 1;
            } else if (areBothSelfIncreasing) {
                state[i][0] = state[i - 1][0];
                state[i][1] = state[i - 1][1] + 1;
            } else { // if (areInterchangeIncreasing)
                state[i][0] = state[i - 1][1];
                state[i][1] = state[i - 1][0] + 1;
            }
        }
        
        return Math.min(state[n - 1][0], state[n - 1][1]);
    }

Optimization
Since current state depends on its previous state only, we may use variables to save states rather than the state array.
Java 0.1

    public int minSwap(int[] A, int[] B) {
        int n = A.length, prevNotSwap = 0, prevSwap = 1;
        
        for (int i = 1; i < n; i++) {
            boolean areBothSelfIncreasing = A[i - 1] < A[i] && B[i - 1] < B[i];
            boolean areInterchangeIncreasing = A[i - 1] < B[i] && B[i - 1] < A[i];
            
            if (areBothSelfIncreasing && areInterchangeIncreasing) {
                int newPrevNotSwap = Math.min(prevNotSwap, prevSwap);
                prevSwap = Math.min(prevNotSwap, prevSwap) + 1;
                prevNotSwap = newPrevNotSwap;
            } else if (areBothSelfIncreasing) {
                prevSwap++;
            } else { // if (areInterchangeIncreasing)
                int newPrevNotSwap = prevSwap;
                prevSwap = prevNotSwap + 1;
                prevNotSwap = newPrevNotSwap;
            }
        }
        
        return Math.min(prevSwap, prevNotSwap);
    }

Python

    def minSwap(self, A, B):
        n = len(A)
        prevNotSwap = 0
        prevSwap = 1
        for i in range(1, n):
            areBothSelfIncreasing = A[i - 1] < A[i] and B[i - 1] < B[i] 
            areInterchangeIncreasing = A[i - 1] < B[i] and B[i - 1] < A[i]
            if areBothSelfIncreasing and areInterchangeIncreasing:
                newPrevNotSwap = min(prevNotSwap, prevSwap)
                prevSwap = min(prevNotSwap, prevSwap) + 1
                prevNotSwap = newPrevNotSwap
            elif areBothSelfIncreasing:
                prevSwap += 1 
            else: # if areInterchangeIncreasing:
                newPrevNotSwap = prevSwap
                prevSwap = prevNotSwap + 1
                prevNotSwap = newPrevNotSwap
        return min(prevNotSwap, prevSwap)            
