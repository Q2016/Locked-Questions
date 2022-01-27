Question:
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"    

    
Solution: ---    
    
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
      
      
      
Complexity Analysis

Time complexity : O(nlgn)

Although we are doing extra work in our comparator, it is only by a constant factor. 
Therefore, the overall runtime is dominated by the complexity of sort, which is O(nlgn) in Python and Java.

Space complexity : O(n)

Here, we allocate O(n) additional space to store the copy of nums. Although we could do
that work in place (if we decide that it is okay to modify nums), we must allocate O(n) space for t
he final return string. Therefore, the overall memory footprint is linear in the length of nums.

      
