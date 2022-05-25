Question:
Given a sorted array A of unique numbers, find the K-th missing number starting from the 
leftmost number of the array.

Example 1:
Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.

Example 2:
Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,…], hence the third missing number is 8.



 
 
 
 
 
  
Solution: Binary search
 
Seeing the word "sorted" reminds me that there must be some trick to play with. One common thought 
of mine is binary lookup, which is used for quickly, in O(logN), to locate a specific element. And 
it turns out similar thoughts applies to this problem as well.

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:    
   
   
       def getMissingNumCounts(index):
           return nums[index]-nums[0]-index
     
       n=len(nums)
     
       if k>getMissingNumCounts(n-1):
          return nums[-1]+k-getMissingNumCounts(n-1)
     
     
       left=0
       right=n-1
       
       while left<right:
          mid=left+(right-left)//2

          if getMissingNumsCounts(mid)<k:
            left=mid+1
          else:
            right=mid
           
       return nums[right-1]+k-getMissingNumCounts(right-1)
            
            
Time & Space Complexity
Similar to binary lookup, each time I break the input size N to half so the time complexity will be O(logN).

In my above code, I use recursive calling which will stack to store information. This takes 
 up extra space and the space is directly related to the calls which is also O(logN). So the 
 space complexity is O(logN) as well.            
