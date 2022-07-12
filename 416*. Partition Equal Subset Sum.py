Question:
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].  
  
  
  
  
  
  
  
  
Brute-force for the problem has a O(2^n) complexity, with a DFS we can reduce it to O(n*sum(nums)). With a Buttom-up we can do a
O(sum(nums)) complexity
  
Solution: DP, Backtrackin (related to 0/1 knapsack)
  
 https://www.youtube.com/watch?v=IsvocB5BJhw 
  
  
def canPartition(self, nums):
  if sum(nums)%2:
    return False
  
  dp=set()
  dp.add(0)
  target=sum(nums)//2
  
  for i in range(len(nums)-1,-1,-1):
    nextDP=set()
    for t in dp:
      nextDP.add(t+nums[i])
      nextDP.add(t)
    dp=nextDP # i didnt understand this part
    
  return True if target in dp else False
  
  
