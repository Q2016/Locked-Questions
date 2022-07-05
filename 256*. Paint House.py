Question:
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each 
house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of 
painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on… Find the minimum cost to paint all houses.

Sample I/O
Example 1
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
Minimum cost: 2 + 5 + 3 = 10.  
  

  
  
  
Solution:
https://www.youtube.com/watch?v=-w67-4tnH5U

  
class Solution:
  
  def minCost(self, costs):
    
    dp=[0,0,0]
    for i in range(len(costs)):
      dp0=costs[i][0]+min(dp[1], dp[2])
      dp1=costs[i][1]+min(dp[0],dp[2])
      dp2==costs[i][2]+min(dp[0],dp[1])
      dp=[dp0, dp1, dp2]
      
    return min(dp)
  
  
Time complexity: O(n)
Space : O(1)    
