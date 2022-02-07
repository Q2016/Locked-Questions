Question:
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement 
if for every i (1 <= i <= n), either of the following is true:
perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

Example 1:
Input: n = 2, Output: 2
Explanation: 
The first beautiful arrangement is [1,2]: - perm[1] = 1 is divisible by i = 1     - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]: - perm[1] = 2 is divisible by i = 1    - i = 2 is divisible by perm[2] = 1    


Solution: Backtracking

   int count=0;
    
   def countArrangement(int N): 
        if (N == 0) return 0;
        used=(N+1)*[0];
        helper(N, 1, used);
        return count;
    
   def helper(N, pos, used):
        if (pos > N):
            count++
            return
        for (int i = 1; i <= N; i++):
            if (used[i] == 0 && (i % pos == 0 || pos % i == 0)) :
                used[i] = 1;
                helper(N, pos + 1, used);
                used[i] = 0;

