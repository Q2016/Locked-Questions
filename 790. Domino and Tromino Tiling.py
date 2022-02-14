Question:
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
Given an integer n, return the number of ways to tile an 2 x n board.
In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent 
cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Solution: Dynamic Programming (Top-down)
In this approach, we will use the two transition functions as the recurrence relation. Then we 
will create a recursive solution from the top (f(n)) to the bottom 
(base cases described in the algorithm section) since it's generally more intuitive to solve 
dynamic programming problems in a top-down manner. Additionally, to avoid repeat calculations, we 
will memoize the result for each subproblem by storing the calculated results in two maps (f_cache and p_cache). 
Note that in the python implementation, this will be handled automatically by the @cache decorator.

We'll start from f(n) and then dive all the way down to the base cases, f(1), f(2), and p(2).
Use the same definition for ff and pp from the Overview section
f(k): The number of ways to fully cover a board of width kk
p(k): The number of ways to partially cover a board of width kk
Recursion calls will use the results of subproblems and base cases to help us get the final result, f(n).
The stop condition for the recursive calls is when kk reaches a base case (i.e. k <= 2k<=2).
Values for the base cases will be directly returned instead of making more recursive calls.
f(1) = 1
f(2) = 2
p(2) = 1
To avoid repeated computations, we will use 2 hashmaps (f_cache and p_cache) to store calculated values 
for ff and pp. In Python, the built-in @cache wrapper will automatically maintain these hashmaps for us.
If kk is greater than 22, then we will make recursive calls to ff and pp according to the transition function:
f(k) = f(k-1) + f(k-2) + 2 * p(k-1)f(k)=f(k−1)+f(k−2)+2∗p(k−1)
p(k) = p(k-1) + f(k-2)p(k)=p(k−1)+f(k−2)
f(n) will be returned once all recursive calls are finished.


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007
        @cache  
        def p(n):  
            if n == 2:
                return 1
            return (p(n - 1) + f(n - 2)) % MOD
        @cache  
        def f(n):  
            if n <= 2:
                return n
            return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % MOD

        return f(n)
