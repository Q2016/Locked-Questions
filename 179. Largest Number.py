Question:
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"    

    
nums=[3,30,34,5,9]
Output: "9534330"
    
    
    
    
    
    
    
    
    
    
Solution: Greedy
https://www.youtube.com/watch?v=WDx6Y4i4xJ8    
        
class Solution:
    def largestNumber(self, nums):
        
        for i, n in enumerate(nums):
            nums[i]=str(n)
            
        def compare(n1, n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
            
        nums=sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))
      
      
      
Complexity Analysis

Time complexity : O(nlgn)

Although we are doing extra work in our comparator, it is only by a constant factor. 
Therefore, the overall runtime is dominated by the complexity of sort, which is O(nlgn) in Python and Java.

Space complexity : O(n)

Here, we allocate O(n) additional space to store the copy of nums. Although we could do
that work in place (if we decide that it is okay to modify nums), we must allocate O(n) space for t
he final return string. Therefore, the overall memory footprint is linear in the length of nums.

      
