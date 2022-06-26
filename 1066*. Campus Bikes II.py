Question:
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. 
Each worker and bike is a 2D coordinate on this grid.
We assign one unique bike to each worker so that the sum of the Manhattan distances 
between each worker and their assigned bike is minimized.
The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

Ex1: Input: 
workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 
6
Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.




Solution: (This problem is solved with bit-mask)
  
  https://www.youtube.com/watch?v=x9iOjex5CNE
    
    
    
    

  To learn more about bit-mask: https://www.youtube.com/watch?v=685x-rzOIlY&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g&index=3

  
Let's first solve:
1434. Number of Ways to Wear Different Hats to Each Other (Hard)

There are n people and 40 types of hats labeled from 1 to 40.
Given a 2D integer array hats, where hats[i] is a list of all hats preferred by the ith person.
Return the number of ways that the n people wear different hats to each other.
Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to choose hats given the conditions. 
First person choose hat 3, Second person choose hat 4 and last one hat 5.
  
I started with normal dp to assign people with hats, and got TLE all the time, even though I tried different ways to optimize. 
Then I realized the number of hats is much bigger than the number of people, so I switched to assign hats to people, and of course it worked.

The difference betwen the two is that when assigning people with hats, since hat number is much bigger, we won't hit many duplicate assignments, 
hence less pruning, baiscally we have 40 bit mask and only 10 bit will be set at most; when we assign hats to people, the mask is only 10 bit 
and at most 40 recursion to set the bit, it's much more efficient.

https://www.youtube.com/watch?v=SlwENy96xdE
  
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        htop = [[] for i in range(41)] # htop: hat to people list
        for p, hat_list in enumerate(hats):
            for h in hat_list:
                h2p[h].append(p) # assigning people to hats
        
        def dp(h, mask):
          if (h, mask) in memo:
            return memo[(h, mask)]
  
          if mask ==(1<<n)-1:
            return 1
  
          if h>40: # we are out of hats
            return 0
  
          ans=dp(h+1, mask) #not wearing the current hat
    
          if h in h2p:
            peoples=h2p[h]
            
            for p in peoples:
              if mask & (1<<p)==0:
                # backtracking part
                mask |= (1<<p)
                ans+=dp(h+1, mask)
                mask ^=(1<<p)# revert back to the original
    
          memo[(h, mask)]=ans
      
          return ans
        
        memo={}
        
        return dp(0,0)
  
  
      
For this problem: (top-down)
https://www.youtube.com/watch?v=x9iOjex5CNE    
  
  
def assignBikes(workers, bikes)  :
  
  def getDist(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
  
  
  def dp(index, mask):
    if (index, mask) in memo:
      return memo[(index, mask)]
    
    
    if index==w:
      return 0
    
    ans=sys.maxsize
    worker=workers[index]
    
    for i in range(b):
      if (1<<i) & mask ==0:  #if i'th bike has not been assigned
        bike=bikes[i]
        dist=getDist(worker,bike)
        
        ans=min(ans, dp(index+1,(1<<i)|mask)+dist)
    
    
    memo[(index, mask)]= ans
    
    return ans
  
  
  memo={}
  
  w=len(workers)
  b=len(bikes)
  
  
  
  
  
  
  
  



