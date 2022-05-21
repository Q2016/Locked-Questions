Question:
https://leetcode.com/problems/knight-dialer/	
	
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally 
and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:
A chess knight can move as indicated in the chess diagram below:
We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).
Given an integer n, return how many distinct phone numbers of length n we can dial.
You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. 
All jumps should be valid knight jumps.


Solution: 	

https://medium.com/hackernoon/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029
	
https://leetcode.com/problems/knight-dialer/discuss/189287/O(n)-time-O(1)-space-DP-solution-%2B-Google-interview-question-writeup	

def knightDialer(self, N):
    # Neighbors maps K: starting_key -> V: list of possible destination_keys
    neighbors = {
        0:(4,6),
        1:(6,8),
        2:(7,9),
        3:(4,8),
        4:(0,3,9),
        5:(),
        6:(0,1,7),
        7:(2,6),
        8:(1,3),
        9:(2,4)
    }
    current_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for _ in range(N-1):
        next_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for src_key in range(10):
            for dst_key in neighbors[src_key]:
                next_counts[dst_key] = (next_counts[dst_key] + current_counts[src_key]) % (10**9 + 7)
        current_counts = next_counts
    return sum(current_counts) % (10**9 + 7)

O(n) time O(1) space DP solution + Google interview question


###########################################################################################################


Second solution: (A lot lengthy but intuitive, my prefered solution)

https://leetcode.com/problems/knight-dialer/discuss/190787/How-to-solve-this-problem-explained-for-noobs!!!	
	
Naive Recursive Code


public static final int max = (int) Math.pow(10, 9) + 7;
	
public int knightDialer(int n) {
   long s = 0;
   //do n hops from every i, j index (the very requirement of the problem)
   for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 3; j++) {
         s = (s + paths(i, j, n)) % max;
      }
   }
   return (int) s;
}

private long paths(int i, int j, int n) {
   // if the knight hops outside of the matrix or to * return 0 
   //as there are no unique paths from here
   if(i < 0 || j < 0 || i >= 4 || j >= 3 || (i == 3 && j != 1)) return 0;
   //trivial case
   if(n == 1) return 1;
   //non trivial case
   long s = paths(i - 1, j - 2, n - 1) % max + // jump to a
            paths(i - 2, j - 1, n - 1) % max + // jump to b
            paths(i - 2, j + 1, n - 1) % max + // jump to c
            paths(i - 1, j + 2, n - 1) % max + // jump to d
            paths(i + 1, j + 2, n - 1) % max + // jump to e
            paths(i + 2, j + 1, n - 1) % max + // jump to f
            paths(i + 2, j - 1, n - 1) % max + // jump to g
            paths(i + 1, j - 2, n - 1) % max; // jump to h
   return s;
}
If you run this code for n = 50 in your favorite programming language, you will realize that it takes at least an hour to get the answer.

This is because this problem not only has similar subproblems but each of those similar subproblems have overlapping subproblems. What does this mean? Let me explain with an example.

As seen in the above trace, a subproblem of 1 (0, 0, 3) is 8 (2, 1, 2).

A subproblem of 3 (0, 2, 3) is also 8 (2, 1, 2) because you can get from 3 to 8 in a single hop.

We have already computed the solution to 8 (2, 1, 2) while computing the solution to 1 (0, 0, 3) and there is no need to re-compute this solution if were to store the solution somewhere in memory. The above recursive solution re-computes the solutions to overlapping subproblems and therefore is highly inefficient (runs in the order of O(3 ^ n) I believe).

Top down Dynamic programming solution

We use dynamic programming and store the solution of each subproblem in M. M is a 3D array and each index of M corresponds to a solution of n. Each n is again stored as a 2D array for (i, j) values.

All this combined, M will store the solution of each paths(i, j, n) call.

Below is the code.

public static final int max = (int) Math.pow(10, 9) + 7;
	
public int knightDialer(int n) {
   // A 3D array to store the solutions to the subproblems
   long M[][][] = new long[n + 1][4][3];
   long s = 0;
   //do n hops from every i, j index (the very requirement of the problem)
   for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 3; j++) {
         s = (s + paths(M, i, j, n)) % max;
      }
   }
   return (int) s;
}

private long paths(long[][][] M, int i, int j, int n) {
   // if the knight hops outside of the matrix or to * return 0 
   //as there are no unique paths from here
   if(i < 0 || j < 0 || i >= 4 || j >= 3 || (i == 3 && j != 1)) return 0;
   if(n == 1) return 1;
   //if the subproblem's solution is already computed, then return it
   if(M[n][i][j] > 0) return M[n][i][j];
   //else compute the subproblem's solution and save it in memory
   M[n][i][j] = paths(M, i - 1, j - 2, n - 1) % max + // jump to a
                paths(M, i - 2, j - 1, n - 1) % max + // jump to b
                paths(M, i - 2, j + 1, n - 1) % max + // jump to c
                paths(M, i - 1, j + 2, n - 1) % max + // jump to d
                paths(M, i + 1, j + 2, n - 1) % max + // jump to e
                paths(M, i + 2, j + 1, n - 1) % max + // jump to f
                paths(M, i + 2, j - 1, n - 1) % max + // jump to g
                paths(M, i + 1, j - 2, n - 1) % max; // jump to h
   return M[n][i][j];
}	

Time complexity: O(N)

There is an article save to computer about this google interview question.
