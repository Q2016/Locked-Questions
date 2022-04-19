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
The idea behind this approach is simple. We try to create all the permutations of numbers from 1 to N. We can fix one number at a particular 
position and check for the divisibility criteria of that number at the particular position. But, we need to keep a track of the numbers which 
have already been considered earlier so that they aren't reconsidered while generating the permutations. If the current number doesn't satisfy 
the divisibility criteria, we can leave all the permutations that can be generated with that number at the particular position. This helps to 
prune the search space of the permutations to a great extent. We do so by trying to place each of the numbers at each position.

We make use of a visited array of size N. Here, visited[i] refers to the i^{th} number being already placed/not placed in the array being formed 
till now(True indicates that the number has already been placed).

We make use of a calculate function, which puts all the numbers pending numbers from 1 to N(i.e. not placed till now in the array), indicated 
by a FalseFalse at the corresponding visited[i] position, and tries to create all the permutations with those numbers starting from the pospos 
index onwards in the current array. While putting the pos^{th} number, we check whether the i^{th} satisfies the divisibility criteria on the go 
i.e. we continue forward with creating the permutations with the number ii at the pos^{th} position only if the number ii and pospos satisfy 
the given criteria. Otherwise, we continue with putting the next numbers at the same position and keep on generating the permutations.



public class Solution {
    int count = 0;
    public int countArrangement(int N) {
        boolean[] visited = new boolean[N + 1];
        calculate(N, 1, visited);
        return count;
    }
    public void calculate(int N, int pos, boolean[] visited) {
        if (pos > N)
            count++;
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (pos % i == 0 || i % pos == 0)) {
                visited[i] = true;
                calculate(N, pos + 1, visited);
                visited[i] = false;
            }
        }
    }
}
