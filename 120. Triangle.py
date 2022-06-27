Question:
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, 
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   _2
  _3 4
 6 _5 7
4 _1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).    

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.













Reminds me of a similar question before this question

Solution: DP 


Given a triangle array, we need to return the path whose sum from top to bottom is minimum.
There is one constraint: we can only move to lower-left or lower-right elements.
For example, in the triangle depicted below, the only valid path from 5 are 5 -> 1 and 5 -> 8. The paths 5 -> 4 or 5 -> 3 are invalid.

   2
  3 4
 6 5 7
4 1 8 3
Now the question is, can we solve it greedily, i.e., simply check the immediate step and choose the smaller element?
The answer is no. Because the current choice will affect the later decisions. This is illustrated in the following example:

   2
  4 5
 6 5 1
4 1 8 2
The greedy strategy will use the path 2 -> 4 -> 5 -> 1. But, the optimal path is 2 -> 5 -> 1 -> 2.
We need to use Dynamic Programming to solve this problem. Solving a problem using DP is generally tricky. This post will help you understand how to develop a DP approach. So, I highly recommend reading all three methods.

❌ Solution I: Recursion [TLE]

We can try all valid paths and calculate the sum. Out of all those, return the minimum sum. At each step, we have two choices:

Move to lower-left element (i + 1 and j)
Move to lower-right element (i + 1 and j + 1)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(i, j):
            if i == len(triangle):
                return 0

            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)

            return min(lower_left, lower_right)

        return dfs(0, 0)
   
   
Time Complexity: O(2ⁿ)
Space Complexity: O(n)
   
   
✅ Solution II: Top-Down DP or Memoization [Accepted]

We are doing a lot of repetitive work in the above recursive solution. How?
Have a look at the above example. The subtree with head 5 is repeated twice. We need to compute the minimum sum path during the first time (2 -> 3 -> 5 -> ...). During the second time from 2 -> 4 -> 5, we can simply use the result from the first time instead of traversing again. This is the essence of memoization.
In Python, it is as simple as adding the @cache decorator. But, this won't be accepted in the interviews and have many limitations.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i == len(triangle):
                return 0

            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)

            return min(lower_left, lower_right)

        return dfs(0, 0)
We can manually use a way to store the information and use it later. Here, two variables (i and j) are changing and can be used to store a state. So, we can use a matrix. The following code will make it clear.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[-1] * len(triangle) for _ in range(len(triangle))]
        def dfs(i, j):
            if i == len(triangle):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)
            memo[i][j] = min(lower_left, lower_right)
            return memo[i][j]

        return dfs(0, 0)
   
Time Complexity: O(n²)
Space Complexity: O(n²)
   
   
Recursion is slower than the iterative approach. So, we can further optimize the above solution by using bottom-up DP.
We can do a bottom-up traversal instead of traversing from top to bottom. Coming up with a bottom-up DP is challenging at first and requires practice. Instead of looking at the bigger problem, we look at smaller sub-problems and try to build up the solution. The following example will help you to understand:

1. Suppose that only the last level is given. 

4 1 8 3

Then what should be your answer?

If you thought 1, then congratulations 🎉 you are correct. This is our first subproblem. 

2. Now, the last two levels are given.

 6 5 7
4 1 8 3

Here, what should be the answer and what information do you need to store?

Clearly, the answer is 6 (5 -> 1). But, this may not be the optimal path. So, we need to store all the optimal paths, i.e.,
[(6 -> 1), (5 -> 1), 7 -> 3)] or [7, 6, 10]. This is our second subproblem.

3. Last 3 levels are given.

  3 4
 6 5 7
4 1 8 3

Again, what should be the answer and what information do you need to store (or use)?

Answer is 9 (3 -> 5 -> 1). Do we need to look again at all the paths? Can we use the information that we previously stored?
No and Yes.
If we replace the triangle as
  3 4
 7 6 10
then also, we'll get the same answer. And we can store this information as [(3 -> 6), (4 -> 6)] or [9, 10].

4. All levels are given

   2
  3 4
 6 5 7
4 1 8 3

Which can be replaced as:
   2
  9 10

And hence, our answer is 11 (2 -> 9)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1] * n for _ in range(n)]
        dp[n - 1] = triangle[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                lower_left = triangle[i][j] + dp[i + 1][j]
                lower_right = triangle[i][j] + dp[i + 1][j + 1]
                dp[i][j] = min(lower_left, lower_right)

        return dp[0][0]
   
   
Time Complexity: O(n²)
Space Complexity: O(n²)
   
   
✅ Solution III (b): Bottom Up DP or Tabulation (Space Optimized) [Accepted]

Notice that we only require the information about the next row. So, instead of creating a 2D matrix, a 1D array is sufficient.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        next_row = triangle[-1][:]
        curr_row = [0] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                lower_left = triangle[i][j] + next_row[j]
                lower_right = triangle[i][j] + next_row[j + 1]
                curr_row[j] = min(lower_left, lower_right)

            curr_row, next_row = next_row, curr_row

        return next_row[0]  # because we swapped at last iteration
   
Time Complexity: O(n²)
Space Complexity: O(n)   
   
   
   
I think below that's from NeetCode is much simpler than Solution III (b): Bottom Up DP:

from: https://www.youtube.com/watch?v=OM1MTokvxs4
      
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
         dp=[0]*(len(traingle)+1)
         
         for row in triangle[::-1]:
            for i,n in enumerate(row):
               dp[i]=n+min(dp[i], dp[i+1])
         
         return dp[0]
      
