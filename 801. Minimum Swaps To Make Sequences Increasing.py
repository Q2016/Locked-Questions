Explanation
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
   
   
   
   more comments:
   
   
        
public int minSwap(int[] A, int[] B) {
        int[] noSwap = new int[A.length];
        int[] swap = new int[A.length];
        swap[0] = 1;
        for (int i=1; i<A.length; ++i) {

            // This is max value, could be anything as long as they are higher
            // than max possible value (which would be A.length-1, since max
            // swaps you can do is A.length-1)
            noSwap[i] = A.length; swap[i] = A.length;

            if (A[i]>A[i-1] && B[i]>B[i-1]) {
                // We are here because this index does not need to swap.

                // Great, what would be the cost to reach here and not swap?
                // It'll be same as cost of not swapping for prev. index.
                // Why dont we rather take min(noSwap[i-1], swap[i-1]), because
                // in that case noSwap[i-1] will be min anyway.
                noSwap[i] = noSwap[i-1];


                // what would be the cost to reach here and swap?
                // It'll be cost of swapping for prev. index + 1.
                // Why dont we rather take min(noSwap[i-1], swap[i-1]) + 1, because
                // we are tracking optimistic swaps and if we do min, we will lose
                // track of swaps that were needed and done in past.
                swap[i] = swap[i-1] + 1;

            } else {
                // This index needs to be swapped, so lets keep max values for current swap
                // and noSwap values.
            }

            if (A[i]>B[i-1] && B[i]>A[i-1]) {
                // We are here because this index is a candidate of swapping
                // and keeping the seq increasing.
                // If swapping is not needed then being here will be noop, since
                // we are using min of values we set in prev if statement and value we
                // will set here in pessimistic case

                // what would be the cost to reach here and not swap?
                // It'll be min of:
                //      cost of swapping for prev. index
                //      or cost of not swapping prev index.
                // The catch is that if swapping is needed then
                // (noSwap[i] == A.length) > swap[i-1]
                // And if swapping is not needed then,
                // noSwap[i] will be set in prev. if statement and
                // will be less than swap[i-1]
                noSwap[i] = Math.min(noSwap[i], swap[i-1]);


                // what would be the cost to reach here and swap?
                // It'll be min of:
                //      cost of not swapping for prev. index + 1
                //      or cost of swapping this index.
                // The catch is that if swapping is needed then
                // (swap[i] == A.length) > (noSwap[i-1]+1)
                // And if swapping is not needed then,
                // swap[i] will be set in prev. if statement and
                // will _still_ be more than (noSwap[i-1]+1)
                //
                // so can this be replaced with: swap[i] = noSwap[i-1]+1;
                swap[i] = Math.min(noSwap[i-1]+1, swap[i]);


            } else {
                // This index can't be swapped so we will keep the values
                // from previous if statement.

                // Note that it's given in question that there wiill be no invalid
                // cases, so in every case code will enter at least one if statement.
            }


        }

        // Now that we cost of swapping and not swapping each index,
        // answer is:
        return Math.min(noSwap[A.length-1], swap[A.length-1]);
        
 
       
        
        
        
